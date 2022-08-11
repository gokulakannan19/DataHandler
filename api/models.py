from multiprocessing.sharedctypes import Value
from django.db import models
from django.utils.crypto import get_random_string
import uuid

# Create your models here.


class Account(models.Model):
    token = get_random_string(length=32)
    email_id = models.EmailField(unique=True, max_length=255)
    account_name = models.CharField(max_length=255)
    app_secret_token = models.CharField(
        max_length=255, unique=True, blank=True)
    account_id = models.UUIDField(default=uuid.uuid4, unique=True,
                                  primary_key=True, editable=False)
    website = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.app_secret_token = get_random_string(length=32)
        super(Account, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.account_name


class Destination(models.Model):
    url = models.URLField()
    http = models.CharField(max_length=255)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Headers(models.Model):
    app_id = models.CharField(max_length=255)
    app_secret = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255, default="application/json")
    accept = models.CharField(max_length=255, default="*")
    destination = models.OneToOneField(
        Destination, primary_key=True, on_delete=models.CASCADE)


class DataHandler(models.Model):
    data = models.CharField(max_length=255)
