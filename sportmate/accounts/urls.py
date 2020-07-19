from django.urls import path, include
from . import views



urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("settings/", views.settings, name="settings"),
    path("change-password/", views.change_password, name="change-password"),
    path("change-data/", views.change_basic_data, name="change-data")
]