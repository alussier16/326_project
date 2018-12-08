import datetime
import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
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
    if useraccount not in friends:
        posts += useraccount.post_set.all()
    posts = sorted(posts, key=lambda x: x.time_stamp, reverse=True)[:30]

    if request.method == "POST":
        if 'new_comment_post' in request.POST and 'new_comment' in request.POST and request.POST['new_comment']!=None:
            post = get_object_or_404(Post, pk=request.POST['new_comment_post'])
            comment = Comment()
            comment.author = auth.get_user(request).useraccount
            comment.time_stamp = datetime.datetime.now()
            comment.content = request.POST['new_comment']
            comment.post = post
            comment.save()
        if 'react1' in request.POST:
            post = get_object_or_404(Post, pk=request.POST['react1'])
            try:
                old_react = Reaction.objects.get(post=post.id, user=auth.get_user(request).useraccount)
            except:
                old_react = None
            if not old_react == None:
                old_react.delete()
            reaction = Reaction(user=auth.get_user(request).useraccount, status=1, post=post, time_stamp = datetime.datetime.now())
            reaction.save()
        elif 'react2' in request.POST:
            post = get_object_or_404(Post, pk=request.POST['react2'])
            try:
                old_react = Reaction.objects.get(post=post.id, user=auth.get_user(request).useraccount)
            except:
                old_react = None
            if not old_react == None:
                old_react.delete()
            reaction = Reaction(user=auth.get_user(request).useraccount, status=2, post=post, time_stamp = datetime.datetime.now())
            reaction.save()
        elif 'react3' in request.POST:
            post = get_object_or_404(Post, pk=request.POST['react3'])
            try:
                old_react = Reaction.objects.get(post=post.id, user=auth.get_user(request).useraccount)
            except:
                old_react = None
            if not old_react == None:
                old_react.delete()
            reaction = Reaction(user=auth.get_user(request).useraccount, status=3, post=post, time_stamp = datetime.datetime.now())
            reaction.save()
        elif 'react4' in request.POST:
            post = get_object_or_404(Post, pk=request.POST['react4'])
            try:
                old_react = Reaction.objects.get(post=post.id, user=auth.get_user(request).useraccount)
            except:
                old_react = None
            if not old_react == None:
                old_react.delete()
            reaction = Reaction(user=auth.get_user(request).useraccount, status=4, post=post, time_stamp = datetime.datetime.now())
            reaction.save()

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

            friend = User.objects.get(username = form.cleaned_data).useraccount
            print(friend)
            user.useraccount.friends.add(friend)
            user.useraccount.save()

        return render(
            request, 'add-friend.html', {'page': 'settings', 'user': user, 'form': form}
        )
    else:
        form = AddFriendForm()
        return render(
            request, 'add-friend.html', {'page': 'settings', 'user': user, 'form': form}
        )

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


def getpost(request, post_number):
    user=UserAccount.objects.get(pk=1)
    friends = user.friends.all()
    posts = []
    print("Post number is ", post_number)
    for friend in friends:
        posts += friend.post_set.all()

    posts = sorted(posts, key=lambda x: x.time_stamp, reverse=True)[post_number: 10 + post_number]
    print("posts", posts)
    updated_posts = []
    for post in posts:
        comments = []
        reactions = [0, 0, 0, 0]
        for reaction in post.reaction_set.all():
            for i in range(1, 5):
                if(int(reaction.status) == i):
                    reactions[i - 1] = (reactions[i - 1] + 1)
        maxVal = max(max(reactions), 1)
        reactions = list(map(lambda x: max(1, int(((x/maxVal) * 100))), reactions))
        print(reactions)
        # print(reactions)
        for comment in post.comment_set.all():
            comments.append({"author": str(comment.author), "content": comment.content})
        updated_posts.append({
            "author": post.author.user.username,
            "text_content": post.text_content,
            "comments": comments,
            "reactions": reactions})

    print(updated_posts[0])
    data = {}
    # data["posts"] = serializers.serialize('json', updated_posts)
    data["posts"] = json.dumps(updated_posts)
    return JsonResponse(data)
