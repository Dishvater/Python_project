from django.contrib import admin
from smate.models import User, Event

# Register your models here.

admin.site.register(User)
admin.site.register(Event)

# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
    # fields =