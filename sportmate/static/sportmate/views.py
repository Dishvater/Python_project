from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View

from smate.models import Event


def home(request):
    return render(request, 'home.html')


@login_required
class PanelView(View):
    event = "pier..."

    def get(self, request):
        # event = Event.objects.all()
        # return render(request, "panel.html")
        return render(request, 'panel.html', {'event': self.event})
