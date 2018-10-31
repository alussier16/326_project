from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from closeknit.models import UserAccount, Post, Comment, Reaction

# Create your views here.
def test(request):
    return HttpResponse('Welcome to Closeknit')

def post(request):
    user = UserAccount.objects.get(pk=1)
    friends = user.friends.all()
    posts=[]
    for friend in friends:
        posts += friend.post_set.all()
    posts = sorted(posts, key=lambda x: x.time_stamp, reverse=True)[:30]
    return render(
        request, 'post.html', {'posts': posts, 'page': 'main'}
    )

def account(request):
    user = UserAccount.objects.get(pk=1)
    posts = sorted(user.post_set.all(), key=lambda x: x.time_stamp, reverse=True)[:30]
    return render(
        request, 'post.html', {'posts': posts, 'page': 'account'}
    )

def ties(request):
    return render(
        request, 'ties.html', {'page': 'ties'}
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
