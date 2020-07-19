from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


def add_event(request):
    return render(request, 'addevent.html')


@login_required
def panel(request):
    return render(request, 'panel.html')

