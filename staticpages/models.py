from django.db import models


class Skills(models.Model):

    skill_name = models.CharField(max_length=50)
    skill_percent = models.CharField(max_length=50)
    skill_class = models.CharField(max_length=50)