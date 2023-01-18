from django.db import models

class Make(models.Model):
    link = models.CharField(max_length=9999)
    uuid = models.CharField(max_length=10, null=True)
