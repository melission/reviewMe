from django.http import HttpResponse
from django.shortcuts import render
from books.models import *
from movies.models import *
from templates import *


def index(request):
    # http://127.0.0.1:8000/?name=True shows True page
    # http://127.0.0.1:8000/?name=    [with spaces] is being considered as an empty str
    # http://127.0.0.1:8000/?name='       ' turned out as name=''
    # name = request.GET.get("name") or "index"
    # return HttpResponse(f'{name} page')
    # return render(request, 'index.html', {'name': name})
    book_amount = Book.objects.count()
    movie_amount = Movie.objects.count()
    massage = f'On the site {book_amount} titles of books and {movie_amount} names of movies'
    return render(request, context={'message': massage}, template_name='index.html')
