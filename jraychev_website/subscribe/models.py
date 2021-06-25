from django.db import models
from django.utils import timezone


class Subscribe(models.Model):

    email = models.EmailField(max_length=50)
    date_submitted = models.DateTimeField(default=timezone.now)