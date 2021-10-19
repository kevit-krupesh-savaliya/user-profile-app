from django.db import models


class User(models.Model):
    name = models.CharField(max_length=60, blank=False)
    email = models.CharField(max_length=60, blank=False, unique=True)
    phone_no = models.FloatField(max_length=10, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=6, default='Male')

    def __str__(self):
        return self.name
