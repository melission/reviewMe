from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *


# Create your views here.
def books_all(request):
    book_count = Book.objects.count()
    return render(request=request, context={'context': f"there are {book_count} books has found"},
                  template_name='books.html')

# class BookHomePage(TemplateView):
#     template_name = 'books.html'

def book_search(request):
    # http://127.0.0.1:8000/books/search/?search_phrase=%27another%20good%20book%20to%20read%27
    search = request.GET.get("search_phrase") or 'one marvelous book'
    return render(request, 'search_result_books.html', {'search_phrase': search})

