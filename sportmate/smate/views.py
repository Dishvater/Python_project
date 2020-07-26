from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import CreateView

from smate.forms import UserForm, EventForm
from smate.models import User, Event
from rest_framework import viewsets

from smate.serializers import EventSerializer


def main_site_template(request):
    return render(request, "index.html", {})


def my_events(request):
    # event = Event.objects.get(pk=event_id)
    # event = Event.objects.all()
    event = "i ch..."
    return render(request, "panel.html", {'event': event})


def Add_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "addevent", context)


class PanelView(View):

    event = Event.objects.all()
    def get(self, request):

        # return render(request, "panel.html")
        # import ipdb
        # ipdb.set_trace()
        return render(request, 'panel.html', {'events': self.event})


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class PostCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = "/user/add"
    template_name = "add.html"


class AddEventView(CreateView):
    model = Event
    form_class = EventForm
    success_url = "/addevent"
    template_name = "addevent.html"
