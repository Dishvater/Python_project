from django.db import models

# Create your models here.


class User(models.Model):
    email = models.TextField(max_length=128)
    password = models.TextField(max_length=128)
    name = models.TextField(max_length=128)
    surname = models.TextField(max_length=128)
    date_of_birth = models.DateTimeField(max_length=10, null=True, blank=True)
    phone = models.TextField(max_length=128)

    def __str__(self):
        return self.name
