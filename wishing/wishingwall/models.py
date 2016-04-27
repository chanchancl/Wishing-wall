from django.db import models

# Create your models here.

class Wishing(models.Model):
    wID = models.IntegerField()
    wText = models.CharField(max_length=100)