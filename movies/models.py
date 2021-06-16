from django.db import models


# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    # poster = models.ImageField()
    released_at = models.IntegerField()
    description = models.CharField(max_length=1000)
    directors = models.ManyToManyField('Directors', through='MovieDirectors')
    actors = models.ManyToManyField('Actors', through='MovieActors')
