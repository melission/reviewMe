from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.
def movies_all(request):
    # movie_amount = Movie.objects.count()
    movies = Movie.objects.all()
    movie_list = []

    for movie in movies:
        movie_list.append({
            'id': movie.id,
            'title': movie.title,
            'released_at': movie.released_at,
            'actors': movie.actors,
            'directors': movie.directors,
            'description': movie.description,
            'writers': movie.writers,
        })

    return render(request, 'movie_list.html',
                  context={'movie_list': movie_list})

def detailed_movie(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'detailed_movie.html', context={'movie': movie})