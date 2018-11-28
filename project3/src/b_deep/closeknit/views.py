import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib import auth
from closeknit.models import UserAccount, Post, Comment, Reaction
from closeknit.forms import AddFriendForm, SettingsEmailForm, SettingsUsernameForm, SettingsFriendCodeForm, SettingsPasswordForm, SignUpForm, CommentForm, PostForm


from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def test(request):
    return HttpResponse('Welcome to Closeknit')

@login_required(login_url='login')
def post(request):
    user=User.objects.get(pk=request.user.id)
    useraccount = user.useraccount
    friends = useraccount.friends.all()
    posts=[]
    for friend in friends:
        posts += friend.post_set.all()
    posts = sorted(posts, key=lambda x: x.time_stamp, reverse=True)[:30]

    return render(
        request, 'post.html', {'posts': posts, 'page': 'main', 'user': user}
    )

@login_required(login_url='login')
def account(request, viewed_account):
    user=User.objects.get(pk=request.user.id)
    viewed_user = User.objects.get(username=viewed_account)
    posts = sorted(viewed_user.useraccount.post_set.all(), key=lambda x: x.time_stamp, reverse=True)[:30]
    return render(
        request, 'post.html', {'posts': posts, 'page': 'account', 'user': user}
    )

@login_required(login_url='login')
def ties(request):
    user=User.objects.get(pk=request.user.id)
    friends = user.useraccount.friends.all()
    return render(
        request, 'ties.html', {'page': 'ties', 'user': user, 'friends': friends}
    )

def log_in(request):
    if request.user.is_authenticated:
        return redirect('main')
    if ('username' in request.POST):
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')

    return render(
        request, 'registration/login.html', {'page': 'login'}
    )

def log_out(request):
    logout(request)
    return render(
        request, 'registration/logout.html', {'page': 'logout'}
    )

def signup(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            newUser = User(first_name=form.cleaned_data['fname'],
                            last_name=form.cleaned_data['lname'],
                            email=form.cleaned_data['email'],
                            username=form.cleaned_data['username'],is_superuser=False)
            newUser.set_password(form.cleaned_data['password'])
            newUser.save()

            profile = UserAccount(user=newUser,friend_code=form.cleaned_data['friend_code'])
            profile.save()
            login(request, newUser)
            return redirect('accountcreated')

    return render(
        request, 'sign-up.html', {'page': 'sign-up'}
    )

def accountcreated(request):
    return render(
        request, 'account-created.html', {'page': 'account-created'}
    )

@login_required(login_url='login')
def settings(request):
    user = User.objects.get(pk=request.user.id)
    fno = 0  #this is used in settings template to decide which error to display

    #if email is being updated
    if request.method == 'POST' and 'btnEmail' in request.POST:

        form = SettingsEmailForm(request.POST)
        fno = 1
        if form.is_valid():
            user.email = form.cleaned_data
            user.save()

    #if username is being updated
    elif request.method == 'POST' and 'btnUsername' in request.POST:
        form = SettingsUsernameForm(request.POST)
        fno = 2
        if form.is_valid():
            user.username = form.cleaned_data
            user.save()

    #if friend code is being updated
    elif request.method == 'POST' and 'btnFriendCode' in request.POST:

        form = SettingsFriendCodeForm(request.POST)
        fno = 3
        if form.is_valid():
            user.useraccount.friend_code = form.cleaned_data
            user.useraccount.save()

    #if password is being updated
    elif request.method == 'POST' and 'btnPassword' in request.POST:

        form = SettingsPasswordForm(request.POST)
        fno = 4
        if form.is_valid():
            print("password form valid")
            user.set_password(form.cleaned_data)
            user.save()

    else:
        fno = 0
        form = SettingsEmailForm()
        form = SettingsUsernameForm()
        form = SettingsFriendCodeForm()
        form = SettingsPasswordForm()


    context = {'page': 'settings', 'user': user, 'form': form, 'fno': fno}

    return render(request, 'settings.html', context)



    """ TRIAL THAT WORKS ONLY FOR EMAIL i.e if one form on page
    user = UserAccount.objects.get(pk=1)

    if request.method == 'POST':

        form = SettingsEmailForm(request.POST)

        if form.is_valid():
            user.email = form.cleaned_data
            user.save()
            return HttpResponse("amk email saved")

    else:
        form = SettingsEmailForm()

    context = {'page': 'settings', 'user': user, 'form': form}

    return render(request, 'settings.html', context)

    #return render(request, 'settings.html', {'page': 'settings', 'user': user})
    """

@login_required(login_url='login')
def addfriend(request):
    user=User.objects.get(pk=request.user.id)
    
    
    if request.method == 'POST':

        form = AddFriendForm(request.POST)

        if form.is_valid():
            friend = User.objects.get(username = form.cleaned_data.get('username')).useraccount
            user.useraccount.friends.append(friend)
            user.useraccount.save()
        
            
        return render(
            request, 'add-friend.html', {'page': 'settings', 'user': user, 'form': form} 
        )
    else:
        form = AddFriendForm()
        return render(
            request, 'add-friend.html', {'page': 'settings', 'user': user, 'form': form} 
        )

def add_comment(request, pk):
    print(request)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.author = auth.get_user(request).useraccount
            comment.time_stamp = datetime.datetime.now()
            comment.content = form.cleaned_data['content']
            comment.post = post
            comment.save()
            return redirect('main')
    else:
        form = CommentForm()
    return render(request, 'add-comment.html', {'form': form})

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.author = auth.get_user(request).useraccount
            post.time_stamp = datetime.datetime.now()
            post.text_content = form.cleaned_data['text_content']
            post.save()
            return redirect('main')
    else:
        form = PostForm()
    return render(request, 'add-post.html', {'form': form})
