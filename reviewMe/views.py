from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from books.models import *
from movies.models import *
from templates import *
from .forms import SearchForm


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


def bookSearch(search):
    book_found = Book.objects.filter(title__icontains=search)
    return book_found


def contribSearch(search):
    author_found = Contributor.objects.filter(
        Q(last_name__contains=search) | Q(first_name__contains=search))
    return author_found


def movieSearch(search):
    movie_found = Movie.objects.filter(title__icontains=search)
    return movie_found


def directorSearch(search):
    directors_found = Directors.objects.filter(Q(last_name__contains=search) | Q(first_name__contains=search))
    return directors_found


def searchField(request):
    # http://127.0.0.1:8000/books/search/?search_phrase=%27another%20good%20book%20to%20read%27
    search = request.GET.get("search_phrase") or 'one marvelous book'
    form = SearchForm(request.GET)
    search_in = request.GET.get('search_in')
    result = []
    # print(f'search_in {search_in}')
    search_result = []
    if search_in is None:
        result = {}
        result['books'] = bookSearch(search)
        result['movies'] = movieSearch(search)
        result['authors'] = contribSearch(search)
        result['directors'] = directorSearch(search)
        print(result)
        pass
    elif search_in == 'Book':
        result = bookSearch(search)
        # try:
        # except Book.DoesNotExist:
        #     search_result = [f'There is no book with the name {search}']
    elif search_in == 'Contributor':
        result = contribSearch(search)
        # try:
        #     search_result.append([Contributor.objects.get(last_name__contains=search)])
        # except Contributor.DoesNotExist:
        #     pass
        # try:
        #     search_result.append([Contributor.objects.get(first_name__contains=search)])
        #     print(search_result)
        # except Contributor.DoesNotExist:
        #     search_result = [f'There is no author with the name {search}']
        # try:
        # except Contributor.DoesNotExist:
        #     search_result.append(f'There is no author named {search}')
    elif search_in == 'Movie':
        result = movieSearch(search)
    elif search_in == 'Director':
        result = directorSearch(search)
    if len(result) > 0:
        search_result = [x for x in result]
    elif len(result) == 0:
        search_result = [f'Nothing has been found on {search}']
    return render(request, 'search_result.html',
                  {'form': form, 'search_phrase': search, 'search_result': search_result})
