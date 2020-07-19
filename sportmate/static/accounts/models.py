from django.db import models


class User(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(max_length=10, null=True, blank=True)
    phone = models.IntegerField(max_length=15)

    def __str__(self):
        return f' self.first_name, self.last_name'



