from django.shortcuts import render
from django.db.models import Q
from books.models import Book, Review, BookContributor
from .utils import average_rating
# Create your views here.


def book_list_page(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = Review.objects.all()
        authors = []
        contributors = book.contributors.filter(Q(bookcontributor__role='AUTHOR') | Q(bookcontributor__role='CO_AUTHOR'))
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
