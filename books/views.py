from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *
from .forms import ReviewForm


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
    return render(request, 'search_result_books.html', {'search_phrase': search})

