from django.urls import path, include
from . import views


urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.register, name="signup"),
    path("settings/", views.settings, name="settings"),
    path("change-password/", views.change_password, name="change-password"),
    path("change-data/", views.change_basic_data, name="change-data"),
]
