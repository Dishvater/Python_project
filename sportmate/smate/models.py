from django.db import models
from accounts.models import User


class City(models.Model):
    city = models.CharField(max_length=128)

    def __str__(self):
        return self.city


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
    users = models.OneToOneField(User, blank=True, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.what



