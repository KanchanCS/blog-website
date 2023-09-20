from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm

# Create your views here.


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect("account:login")
    else:
        form = RegisterForm()

    context = {
        "form": form,
    }
    return render(request, "signup.html", context)


def Login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect("blog:index")

    else:
        form = LoginForm()

    context = {"forms": form}
    return render(request, "login.html", context)


def Logout(request):
    logout(request)
    return redirect("blog:index")
