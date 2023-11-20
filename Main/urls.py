from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage, name="home"),
    path("login", login_page, name="login"),
    path("login/sso", login_sso, name="login_sso"),
    path("login/sso/code", login_sso_code, name="login_sso_code"),
    path('logout/', logout_user, name='logout')
]
