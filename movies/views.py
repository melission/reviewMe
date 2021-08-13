from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import HttpResponse


# Create your views here.
def movies_all(request):
    # movie_amount = Movie.objects.count()
    movies = Movie.objects.all()
    movie_list = []

    for movie in movies:
        directors = movie.directors.filter(
            Q(moviedirectors__role='DIRECTOR') | Q(moviedirectors__role='ONE OF THE DIRECTORS'))
        actors = movie.actors.filter(
            Q(movieactors__role='MAIN_ACTOR') | Q(movieactors__role='SUPPORTING_ROLE')
        )
        writers = movie.writers.filter(
            Q(moviewriters__role='AUTHOR') | Q(moviewriters__role = 'CO_AUTHOR')
        )
        movie_list.append({
            'id': movie.id,
            'title': movie.title,
            'released_at': movie.released_at,
            'actors': actors,
            'directors': directors,
            'description': movie.description,
            'writers': writers,
        })

    return render(request, 'movie_list.html',
                  context={'movie_list': movie_list})


def detailed_movie(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'detailed_movie.html', context={'movie': movie})
