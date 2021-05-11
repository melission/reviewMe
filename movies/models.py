from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=64)
    # poster = models.ImageField()
    released_at = models.IntegerField()
    description = models.CharField(max_length=1000)

