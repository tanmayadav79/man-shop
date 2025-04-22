from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def Sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirects to Instamart homepage
        else:
            messages.error(request, 'Invalid form submission, try again.')
    else:
        form = UserCreationForm()
    return render(request, 'Register/Signup.html', {'form': form})


def Sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirects to Instamart homepage
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'Register/Signin.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('signin')  # Redirects to sign-in page after logout
