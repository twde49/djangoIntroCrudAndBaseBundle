from django.db import models


# Create your models here.


class Message(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
