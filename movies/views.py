from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages


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


def add_person(request):
    if request.method == 'GET':
        # print(request.GET)
        model_name = request.GET['model_name']
        if model_name == 'actor':
            form = AddActorForm()

        if model_name == 'writer':
            form = AddDirectorForm()

        if model_name == 'director':
            form = AddWriterForm()

        return render(request, 'add_person.html', context={'form': form, 'model_name': model_name})
    if request.method == 'POST':
        # print(request.POST)
        model_name = request.POST['model_name']
        # print(f'model name {model_name}')
        if model_name == 'actor':
            form = AddActorForm(request.POST)

        if model_name == 'director':
            form = AddDirectorForm(request.POST)

        if model_name == 'writer':
            form = AddWriterForm(request.POST)

        if form.is_valid():
            saved_form = form.save()
            messages.success(request, f' {saved_form.first_name} {saved_form.last_name} has been successfully added')
        return render(request, 'add_person.html', context={'form': form, 'model_name': model_name})

