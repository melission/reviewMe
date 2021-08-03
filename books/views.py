from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Q
from .models import *
from .forms import *
from reviews.utils import average_rating


# Create your views here.
# def books_all(request):
#     book_count = Book.objects.count()
#     book_list = Book.objects.all()
#     return render(request=request, context={'context': f"there are {book_count} books have being found",
#                                             'book_list': book_list},
#                   template_name='books.html')


# class BookHomePage(TemplateView):
#     template_name = 'books.html'

# path /books/details/<int:id>
def detailed_book_view(request, id):
    form = ReviewForm()
    book = Book.objects.get(id=id)
    contributors = book.contributors.filter(
        Q(bookcontributor__role='AUTHOR') | Q(bookcontributor__role='CO_AUTHOR')
    )
    context = {'book': book, 'form': form, 'contributors': contributors,
               "description": book.description, "publisher": book.publisher, "published_at": book.published_at}
    # get a book based on id
    if request.method == 'GET':
        return render(request, context=context,
                      template_name='detailed_book_view.html')

    # add a review
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            pass
        # print(form.cleaned_data)
        return render(request, context=context, template_name='detailed_book_view.html')


# path /books/
# show every single book
def book_list_page(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = Review.objects.all()
        authors = []
        contributors = book.contributors.filter(
            Q(bookcontributor__role='AUTHOR') | Q(bookcontributor__role='CO_AUTHOR')
        )
        # for i in range(len(contributors)):
        #     author = contributors[i]
        #     authors.append(author)

        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book,
                          'book_rating': book_rating,
                          'number_of_reviews': number_of_reviews,
                          'publisher': book.publisher,
                          'authors': contributors,
                          'number_of_authors': len(contributors),
                          'id': book.id,
                          'date': book.published_at.year,
                          })
    context = {'book_list': book_list}
    return render(request, 'book_list.html', context=context)


# path /books/publishers/new or /books/publishers/<int:p_id>
# a function that gets a request and either saves data to a new publisher, or retrieves due to p_id an existing one
# p_id is an optional argument; if p_id is None, a new Publisher will be created
def publisher_edit(request, p_id=None):
    # trys to retrieve an existing Publisher based on p_id
    if p_id is not None:
        publisher = get_object_or_404(Publisher, id=p_id)
    else:
        publisher = None

    # creates a new Publisher or gets an existing one
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        # print(form)
        if form.is_valid():
            updated_publisher = form.save(False)
            try:
                pub = Publisher.objects.get(name=updated_publisher.name)
                messages.info(request, f'Publisher {updated_publisher.name} already exists.')
            except Publisher.DoesNotExist:
                updated_publisher = form.save()
                pub = Publisher.objects.get(name=updated_publisher.name)
                messages.success(request, f'Publisher {updated_publisher.name} was created.')
            # if publisher is not None:
            #     messages.success(request, f'Publisher {updated_publisher.name} was updated.')

            return redirect("publisher_edit", pub.id)
    else:
        form = PublisherForm(instance=publisher)

    return render(request, 'publisher_edit.html', {'method': request.method, 'form': form, 'instance': publisher})
