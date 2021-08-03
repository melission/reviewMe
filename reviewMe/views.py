from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from books.models import *
from movies.models import *
from templates import *
from .forms import SearchForm
from itertools import chain
from django.contrib import messages


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
    # search = request.GET.get("search_phrase") or 'one marvelous book'
    form = SearchForm(request.GET)
    if not form.is_valid():
        messages.error(request, 'At least one letter is required.')
        return redirect('main_page')
    if form.is_valid():
        # print(form.cleaned_data)
        search = form.cleaned_data['search_phrase']
        search_in = request.GET.get('search_in')
        search_result = []
        # print(f'search phrase is {search}')
        # print(f'search_in {search_in}')
        if search_in is None:
            books = bookSearch(search)
            movies = movieSearch(search)
            authors = contribSearch(search)
            directors = directorSearch(search)
            # print(search_result)
            search_result = list(chain(books, movies, authors, directors))
        if search_in == 'Book':
            search_result = bookSearch(search)
            # try:
            # except Book.DoesNotExist:
            #     search_result = [f'There is no book with the name {search}']
        if search_in == 'Contributor':
            search_result = contribSearch(search)
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
        if search_in == 'Movie':
            search_result = movieSearch(search)
        if search_in == 'Director':
            search_result = directorSearch(search)
        # print(search_result)

        # # if QuerySey is empty, key is saved with a str as value
        # for key in result.keys():
        #     # print(len(result[key].values()))
        #     if len(result[key].values()) > 0:
        #         # length = len(result[key].values())
        #         # count = 0
        #         search_result[key] = [value for value in result[key].values()]
                # for value in result[key]:
                #     search_result[count] = value
                #     count+=1
                #     print(value)

        # for entry in result:
        #     if result[entry] is None:
        #         pass
        #     else:
        #         search_result[entry] = result[entry]

        # if len(result) > 0:
        #     search_result = [x for x in result]
        # if len(result) > 0:
        #     search_result = [x for x in result]
        # elif len(result) == 0:
        #     search_result[result] = [f'Nothing has been found on {search}']
        # print(search_result)
        return render(request, 'search_result.html',
                      {'form': form, 'search_phrase': search, 'search_result': search_result})
