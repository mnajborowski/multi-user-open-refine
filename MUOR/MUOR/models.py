from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    volume = models.CharField(max_length=64, null=True, blank=True)


class Session(models.Model):
    user = models.OneToOneField(Profile, primary_key=True,
                                on_delete=models.CASCADE)
    port = models.PositiveIntegerField(null=False, unique=True)
    sessionid = models.CharField(max_length=32)
    container_id = models.CharField(max_length=64, null=True, blank=True)

