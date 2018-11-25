from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from closeknit.models import UserAccount, Post, Comment, Reaction
from closeknit.forms import AddFriendForm
from closeknit.forms import SettingsEmailForm
from closeknit.forms import SettingsUsernameForm
from closeknit.forms import SettingsFriendCodeForm
from closeknit.forms import SettingsPasswordForm

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def test(request):
    return HttpResponse('Welcome to Closeknit')

def post(request):
    user=UserAccount.objects.get(pk=1)
    friends = user.friends.all()
    posts=[]
    for friend in friends:
        posts += friend.post_set.all()
    posts = sorted(posts, key=lambda x: x.time_stamp, reverse=True)[:30]

    return render(
        request, 'post.html', {'posts': posts, 'page': 'main', 'user': user}
    )

def account(request, user_account):
    user=UserAccount.objects.get(pk=1)
    viewed_user = UserAccount.objects.get(username=user_account)
    posts = sorted(viewed_user.post_set.all(), key=lambda x: x.time_stamp, reverse=True)[:30]
    return render(
        request, 'post.html', {'posts': posts, 'page': 'account', 'user': user}
    )

def ties(request):
    user=UserAccount.objects.get(pk=1)
    friends = user.friends.all()
    return render(
        request, 'ties.html', {'page': 'ties', 'user': user, 'friends': friends}
    )

def login(request):
    return render(
        request, 'login.html', {'page': 'login'}
    )

def signup(request):
    return render(
        request, 'sign-up.html', {'page': 'sign-up'}
    )

def accountcreated(request):
    return render(
        request, 'account-created.html', {'page': 'account-created'}
    )

def settings(request):
    user = UserAccount.objects.get(pk=1)
    fno = 0  #this is used in settings template to decide which error to display

    #if email is being updated
    if request.method == 'POST' and 'btnEmail' in request.POST:
        
        form = SettingsEmailForm(request.POST)
        fno = 1
        if form.is_valid():
            user.email = form.cleaned_data
            user.save()
            return HttpResponse("amk email saved")

    #if username is being updated
    elif request.method == 'POST' and 'btnUsername' in request.POST:

        form = SettingsUsernameForm(request.POST)
        fno = 2
        if form.is_valid():
            user.username = form.cleaned_data
            user.save()
            return HttpResponse("amk username saved")

    #if friend code is being updated
    elif request.method == 'POST' and 'btnFriendCode' in request.POST:

        form = SettingsFriendCodeForm(request.POST)
        fno = 3
        if form.is_valid():
            user.friend_code = form.cleaned_data
            user.save()
            return HttpResponse("amk friend code saved")

    #if password is being updated
    elif request.method == 'POST' and 'btnPassword' in request.POST:

        form = SettingsPasswordForm(request.POST)
        fno = 4
        if form.is_valid():
            print("password form valid")
            user.password = form.cleaned_data
            user.save()
            return HttpResponse("amk password saved")
   
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

def addfriend(request):
    user=UserAccount.objects.get(pk=1)
    form = AddFriendForm
    return render(
        request, 'add-friend.html', {'page': 'settings', 'user': user, 'form': form} 
    )


