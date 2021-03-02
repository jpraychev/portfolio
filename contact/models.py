from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)
    date_submitted = models.DateTimeField(default=timezone.now)