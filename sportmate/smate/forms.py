from django import forms
from smate.models import User, Event


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ("users",)
