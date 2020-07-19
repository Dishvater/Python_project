from django.db import models


# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=False, blank=False)
    phone = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Event(models.Model):
    what = models.CharField(max_length=128, null=False, blank=False)
    where = models.CharField(max_length=128, null=False, blank=False)
    when = models.DateTimeField(max_length=10, null=False, blank=False)
    minmaxcurrent = models.CharField(max_length=128)
    explevel = models.IntegerField(default=1)
