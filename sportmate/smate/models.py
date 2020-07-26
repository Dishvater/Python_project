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
    LEVEL = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),

    )
    what = models.CharField(max_length=128)
    where = models.CharField(max_length=128)
    when = models.DateTimeField(null=False, blank=False)
    minmaxcurrent = models.CharField(max_length=128)
    explevel = models.IntegerField(choices=LEVEL, default=1)
    users = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.what
