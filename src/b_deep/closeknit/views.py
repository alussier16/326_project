from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse('Welcome to Closeknit')

def main(request):
    return render(
        request, 'main.html'
    )
