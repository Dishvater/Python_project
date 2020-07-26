from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
        ]


class UserBasicDataChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "date_of_birth", "phone"]


class UserPasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        label="Obecne hasło", min_length=8, widget=forms.PasswordInput, required=True
    )
    new_password1 = forms.CharField(
        label="Nowe hasło", min_length=8, widget=forms.PasswordInput, required=True
    )
    new_password2 = forms.CharField(
        label="Powtórz hasło", min_length=8, widget=forms.PasswordInput, required=True
    )

