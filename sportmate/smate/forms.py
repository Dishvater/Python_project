from django import forms
from smate.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User