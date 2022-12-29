from django.db import models
from django.conf import settings
from django.shortcuts import resolve_url


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=6, blank=True)

    def get_absolute_url(self):
        return resolve_url('accounts:profile')