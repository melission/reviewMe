from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.
def movies_all(request):
    movie_amount = Movie.objects.count()
    movie_list = Movie.objects.all()
    return render(request, 'movie_list.html',
                  context={'movie_amount': movie_amount, 'movie_list': movie_list})
