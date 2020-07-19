from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from smate.forms import UserForm, EventForm
from smate.models import User, Event


def main_site_template(request):
    return render(request, "index.html", {})


def Add_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "/addevent.html", context)


class PostCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = "/user/add"
    template_name = "add.html"


class AddEventView(CreateView):
    model = Event
    form_class = EventForm
    success_url = "panel"
    template_name = "addevent"
