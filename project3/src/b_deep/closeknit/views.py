from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from closeknit.models import UserAccount, Post, Comment, Reaction
from closeknit.forms import AddFriendForm, SettingsEmailForm, SettingsUsernameForm, SettingsFriendCodeForm, SettingsPasswordForm, SignUpForm 


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
    logout(request)
    if ('username' in request.POST):
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
    return render(
        request, 'login.html', {'page': 'login'}
    )

def signup(request):
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
    form = AddFriendForm
    return render(
        request, 'add-friend.html', {'page': 'settings', 'user': user, 'form': form} 
    )


