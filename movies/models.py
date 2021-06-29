from django.db import models
# import attr // doesn't work with models.Model


# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    # poster = models.ImageField()
    released_at = models.IntegerField()
    description = models.CharField(max_length=1000)
    directors = models.ManyToManyField('Directors', through='MovieDirectors')
    actors = models.ManyToManyField('Actors', through='MovieActors')
    writers = models.ManyToManyField('Writers', through='MovieWriters')

    def __str__(self):
        return f'{self.title}'


class Directors(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class MovieDirectors(models.Model):
    class DirectorRole(models.TextChoices):
        director = 'DIRECTOR', 'Director'
        co_director = 'ONE OF THE DIRECTORS', 'One of the directors'
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    director = models.ForeignKey(Directors, on_delete=models.CASCADE)
    role = models.CharField(choices=DirectorRole.choices,
                            max_length=20)

    def __str__(self):
        return f'{self.role} {self.director} in {self.movie}'


class Actors(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class MovieActors(models.Model):
    class ActorRole(models.TextChoices):
        main_actor = 'MAIN_ACTOR', 'Main_actor'
        supporting_role = 'SUPPORTING_ROLE', 'Supporting_role'
        # for crowd seen only else supporting role
        other = 'OTHER', 'Other'
        # for cameo only
        cameo = 'CAMEO', 'Cameo'
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actors, on_delete=models.CASCADE)
    role = models.CharField(choices=ActorRole.choices,
                            verbose_name='Supporting role for everyone apart main actors, '
                                         'for crowd seen actors use "other"',
                            max_length=20)

    def __str__(self):
        return f'{self.role} {self.actor} in {self.movie}'


class Writers(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MovieWriters(models.Model):
    class WriterRole(models.TextChoices):
        author = 'AUTHOR', 'Author'
        co_author = 'CO_AUTHOR', 'Co_author'
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    writer = models.ForeignKey(Writers, on_delete=models.CASCADE)
    role = models.CharField(choices=WriterRole.choices,
                            max_length=20)

    def __str__(self):
        return f"{self.role} {self.writer} of {self.movie}"
