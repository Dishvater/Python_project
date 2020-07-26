from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from accounts import forms


def add_event(request):
    return render(request, "addevent.html")


def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/")
        else:
            return render(
                request,
                "registration/signup.html",
                {"form": form, "errors": form.errors},
            )
    else:
        form = forms.RegisterForm()
    return render(request, "registration/signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form": form})


@login_required
def settings(request):
    kwargs = {}
    kwargs["basic_data_change_form"] = forms.UserBasicDataChangeForm(
        prefix="basic_data_change_form", instance=request.user
    )
    kwargs["password_change_form"] = forms.UserPasswordChangeForm(
        prefix="password_change_form"
    )

    return render(request, "settings.html", kwargs)


@login_required
def change_basic_data(request):
    if request.method == "POST":
        form = forms.UserBasicDataChangeForm(
            data=request.POST, prefix="basic_data_change_form", instance=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Dane zostały zmienione.")
        else:
            messages.error(request, "Formularz został wypełniony nieprawidłowo.")
    return HttpResponseRedirect(reverse("settings"))


@login_required
def change_password(request):
    if request.method == "POST":
        form = forms.UserPasswordChangeForm(
            data=request.POST, prefix="password_change_form"
        )
        if form.is_valid():
            cleaned = form.cleaned_data

            old_password = cleaned["old_password"]
            password1 = cleaned["new_password1"]
            password2 = cleaned["new_password2"]

            if password1 == password2 and check_password(
                password=old_password,
                encoded=request.user.password,
                setter=make_password(
                    password=old_password, salt=None, hasher="default"
                ),
            ):
                user = request.user
                user.password = make_password(
                    password=password1, salt=None, hasher="default"
                )
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Hasło zostało zmienione.")
            else:
                messages.error(
                    request,
                    "Obecne hasło jest nieprawidłowe i/lib nowe hasła się nie zgadzają.",
                )
        else:
            messages.error(request, "Formularz został wypełniony nieprawidłowo.")
    return HttpResponseRedirect(reverse("settings"))
