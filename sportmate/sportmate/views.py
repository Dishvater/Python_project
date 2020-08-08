from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from smate.models import Event, City


def home(request):
    event = Event.objects.all()
    city = City.objects.all()
    return render(request, 'home.html', {'events': event, 'cities': city})


def add_event(request):
    return render(request, 'addevent.html')


@login_required
def panel(request):
    return render(request, 'panel.html')


def google_search(request):
    return render(request, "map.html")