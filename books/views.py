from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def books_all(request):
    return render(request=request, template_name='base.html')


def book_search(request):
    # http://127.0.0.1:8000/books/search/?search_phrase=%27another%20good%20book%20to%20read%27
    search = request.GET.get("search_phrase") or 'one marvelous book'
    return render(request, 'search_result_books.html', {'search_phrase': search})
