from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        # User has info and wants account now
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'username already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else: 
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        # GET user wants to enter info
        return render(request, 'accounts/signup.html') 

def login(request):
    return render(request, 'accounts/login.html') 

def logout(request):
    # TODO route to homepage and logout
    return render(request, 'accounts/signup.html') 