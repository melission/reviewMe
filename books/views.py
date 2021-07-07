from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *
from .forms import *


# Create your views here.
def books_all(request):
    book_count = Book.objects.count()
    book_list = Book.objects.all()
    return render(request=request, context={'context': f"there are {book_count} books have being found",
                                            'book_list': book_list},
                  template_name='books.html')

# class BookHomePage(TemplateView):
#     template_name = 'books.html'


def detailed_book_view(request, id):
    if request.method == 'GET':
        book = Book.objects.get(id=id)
        form = ReviewForm()
        return render(request, context={'book': book, 'form': form}, template_name='detailed_book_view.html')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        book = Book.objects.get(id=id)
        if form.is_valid():
            pass
        print(form.cleaned_data)
        return render(request, context={'book': book, 'form': form}, template_name='detailed_book_view.html')


def book_search(request):
    # http://127.0.0.1:8000/books/search/?search_phrase=%27another%20good%20book%20to%20read%27
    search = request.GET.get("search_phrase") or 'one marvelous book'
    form = SearchForm(request.GET)
    search_in = request.GET.get('search_in')
    search_result = []
    if search_in == 'Book':
        try:
            search_result.append([Book.objects.get(title__icontains=search)])
        except Book.DoesNotExist:
            search_result = [f'There is no book with the name {search}']
    elif search_in == 'Contributor':
        try:
            search_result.append([Contributor.objects.get(last_name__contains=search)])
        except Contributor.DoesNotExist:
            pass
        try:
            search_result.append([Contributor.objects.get(first_name__contains=search)])
            print(search_result)
        except Contributor.DoesNotExist:
            search_result = [f'There is no author with the name {search}']
    return render(request, 'search_result_books.html',
                  {'form': form, 'search_phrase': search, 'search_result': search_result})

