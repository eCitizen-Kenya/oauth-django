import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .models import CustomUser


# Create your views here.
def login_page(request):
    return render(request, "login.html")


def login_sso(request):
    return redirect(to=settings.ECITIZEN_LOGIN_URI)


def login_sso_code(request):
    code = request.GET.get("code")
    get_access_token = requests.post(
        settings.ECITIZEN_ACCESS_TOKEN_URL,
        data={
            "client_id": settings.ECITIZEN_CLIENT_ID,
            "client_secret": settings.ECITIZEN_CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": settings.REDIRECT_URL_ON_LOGIN,
        },
    )

    access_token = get_access_token.json()

    get_user_info = requests.get(
        settings.ECITIZEN_USER_INFO_URL,
        params={"access_token": access_token["access_token"]},
    )

    user_info = get_user_info.json()
    updated_user = CustomUser.objects.update_or_create(
        email=user_info["email"],
        id_number=user_info["id_number"],
        account_type=user_info["account_type"],
        first_name=user_info["first_name"],
        last_name=user_info["last_name"],
        surname=user_info["surname"],
        gender=user_info["gender"],
        mobile_number=user_info["mobile_number"],
    )

    user = authenticate(
        request, email=user_info["email"], id_number=user_info["id_number"]
    )

    if user is not None:
        login(request, user)
        return redirect("home")
    else:
        return redirect("login")


@login_required(login_url="login")
def homepage(request):
    return render(request, "home.html")


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect("login")
