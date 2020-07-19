from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from smate.forms import UserForm
from smate.models import User


def main_site_template(request):
    return render(request, "index.html", {})


class PostCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = "/user/add"
    template_name = "add.html"
