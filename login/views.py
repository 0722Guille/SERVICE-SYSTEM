from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required
def index(request):
    return render(request,'index.html')


def signOff(request):
    logout(request)
    return redirect('index')

def start(request):
    return render(request,'start.html')

