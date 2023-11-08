from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'homepage.html')


def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print("user ->", user)
            if user:
                login(request, user)
                return redirect("/")
    return render(request, 'login.html', {'form': form})


def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    return render(request, 'signup.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/login")


@login_required(login_url="/login")
def profile(request):
    return render(request, 'profile.html')
