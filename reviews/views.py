from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from books.forms import ReviewForm
from books.models import Book, Review, BookContributor
from .utils import average_rating
# Create your views here.


def review_edit(request, book_id, review_id=None):
    book = get_object_or_404(Book, id=book_id)
    if review_id is None:
        review = None
    else:
        review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

