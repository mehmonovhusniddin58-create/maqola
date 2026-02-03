from django.db import models

class Userprofile(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    username = models.CharField()
    parol = models.CharField()
