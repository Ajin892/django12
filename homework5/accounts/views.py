from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("counter")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session["visit_count"] = 0
            return redirect("counter")
    else:
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("counter")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            request.session["visit_count"] = 0
            return redirect("counter")
    else:
        form = AuthenticationForm(request)

    return render(request, "accounts/login.html", {"form": form})


@login_required
def counter_view(request):
    count = request.session.get("visit_count", 0) + 1
    request.session["visit_count"] = count
    return render(request, "accounts/counter.html", {"count": count})


@require_POST
def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect("login")
