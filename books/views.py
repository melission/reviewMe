from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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

    # get a book based on id
    if request.method == 'GET':
        book = Book.objects.get(id=id)
        form = ReviewForm()
        return render(request, context={'book': book, 'form': form}, template_name='detailed_book_view.html')

    # add a review
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        book = Book.objects.get(id=id)
        if form.is_valid():
            pass
        print(form.cleaned_data)
        return render(request, context={'book': book, 'form': form}, template_name='detailed_book_view.html')


# a function that gets a request and either saves data to a new publisher, or retrieves due to p_id an existing one
# p_id is an optional argument; if p_id is None, a new Publisher will be created
def publisher_edit(request, p_id=None):

    # trys to retrieve an existing Publisher based on p_id
    if p_id is not None:
        publisher = get_object_or_404(Publisher, id=p_id)
    else:
        publisher = None

    # creates a new Publisher or gets existing one
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        # print(form)
        if form.is_valid():
            updated_publisher = form.save(False)
            try:
                pub = Publisher.objects.get(name=updated_publisher.name)
            except Publisher.DoesNotExist:
                updated_publisher = form.save()
                pub = Publisher.objects.get(name=updated_publisher.name)
            if publisher is None:
                messages.success(request, f'Publisher {updated_publisher.name} was created.')
            else:
                messages.success(request, f'Publisher {updated_publisher.name} was updated.')

            return redirect("publisher_edit", pub.id)
    else:
        form = PublisherForm(instance=publisher)

    return render(request, 'publisher_edit.html', {'method': request.method, 'form': form})
