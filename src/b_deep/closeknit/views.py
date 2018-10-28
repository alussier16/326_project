from django.shortcuts import render
from django.http import HttpResponse

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
