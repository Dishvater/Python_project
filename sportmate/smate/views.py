from django.shortcuts import render

# Create your views here.


def main_site_template(request):
    return render(request, "index.html", {})