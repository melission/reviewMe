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
    writers = models.ManyToManyField('Writers', through='MovieWriters')


class Directors:
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class MovieDirectors:
    class DirectorRole(models.TextChoices):
        director = 'DIRECTOR', 'Director'
        co_director = 'ONE OF THE DIRECTORS', 'One of the directors'
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    director = models.ForeignKey(Directors, on_delete=models.CASCADE)
    role = models.CharField(choices=DirectorRole)


class Actors:
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class MovieActors:
    class ActorRole:
        main_actor = 'MAIN ACTOR', 'Main actor'
        supporting_role = 'SUPPORTING ROLE', 'Supporting role'
        # for crowd seen only else supporting role
        other = 'OTHER', 'Other'
        # for cameo only
        cameo = 'CAMEO', 'Cameo'
    movie = models.ForeignKey(Actors, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actors, on_delete=models.CASCADE)
    role = models.CharField(choices=ActorRole,
                            verbose_name='Supporting role for everyone apart main actors, '
                                         'for crowd seen actors use "other"')


class Writers:
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class MovieWriters:
    class WriterRole:
        author = 'AUTHOR', 'Author'
        co_author = 'CO_AUTHOR', 'Co_author'
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    writer = models.ForeignKey(Writers, on_delete=models.CASCADE)
    role = models.CharField(choices=WriterRole)
