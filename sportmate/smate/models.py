from django.db import models
from accounts.models import User


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
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.what
