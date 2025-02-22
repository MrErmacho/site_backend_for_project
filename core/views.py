from django.shortcuts import render, redirect

from .models import User
from django.contrib.auth import authenticate, login, logout


def signup(request):
    if request.user.is_authenticated:
        return redirect('auth:profile')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')

        exist_user = User.objects.filter(username=username)
        if exist_user:
            return redirect('auth:signup')

        if password != repeat_password:
            return redirect('auth:signup')
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        return redirect('auth:signin')
    return render(request, 'core/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request, username=username, password=password
        )
        if user is not None:
            login(request, user)
            return redirect('auth:profile')
        else:
            return redirect('auth:signup')
        
    return render(request, 'core/signin.html')

def signout(request):
    if not request.user.is_authenticated:
        return redirect('auth:signin')
    logout(request)
    return redirect('auth:signin')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('auth:signin')
    return render(request, 'core/profile.html')