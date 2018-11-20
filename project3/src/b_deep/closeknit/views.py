from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from closeknit.models import UserAccount, Post, Comment, Reaction
from closeknit.forms import AddFriendForm

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
    user=UserAccount.objects.get(pk=1)
    return render(
        request, 'settings.html', {'page': 'settings', 'user': user}
    )

def addfriend(request):
    user=UserAccount.objects.get(pk=1)
    form = AddFriendForm
    return render(
        request, 'add-friend.html', {'page': 'settings', 'user': user, 'form': form} 
    )


