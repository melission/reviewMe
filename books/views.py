from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Q
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
