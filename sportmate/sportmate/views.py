from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from smate.models import Event


def home(request):
    event = Event.objects.all()
    return render(request, 'home.html', {'event': event})


def add_event(request):
    return render(request, 'addevent.html')


@login_required
def panel(request):
    return render(request, 'panel.html')

