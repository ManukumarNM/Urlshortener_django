from django.db import models

# Create your models here.
class Urlshortener(models.Model):
    link = models.CharField(max_length=1000)
    #helps in generating random objects of 128 bits as ids
    uuid = models.CharField(max_length=10)