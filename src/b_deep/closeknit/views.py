from django.shortcuts import render
from django.http import HttpResponse
from closeknit.models import UserAccount, Post, Comment, Reaction

# Create your views here.
def test(request):
    return HttpResponse('Welcome to Closeknit')

def main(request):
    return render(
        request, 'main.html', {'page': 'main'}
    )

def account(request):
    return render(
        request, 'account.html', {'page': 'account'}
    )

def ties(request):
    user = UserAccount.objects.order_by('first_name').first()
    friends_list = user.friends.all()
    friend_count = range(0,friends_list.count())
    context = {
        "user":user,
        "friends_list":friends_list,
        "friend_count":friend_count
    }
    return render(
        request, 'ties.html', context=context
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
