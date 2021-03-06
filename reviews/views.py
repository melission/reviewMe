from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import ReviewBook
from reviews.forms import ReviewBookForm
from books.models import Book
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def book_review_edit(request, id, review_id=None):

    book = get_object_or_404(Book, id=id)

    if review_id is not None:
        edit_review = get_object_or_404(ReviewBook, review_id=review_id)
    else:
        edit_review = None

    form = ReviewBookForm()
    if request.method == 'POST':
        form = ReviewBookForm(request.POST, instance=edit_review)
        if form.is_valid():
            review = form.save(False)
            if review_id is not None:
                review.edited_at = now()
            review.book = book
            review.save()
            if review_id is None:
                messages.success(request, f"Your review has been published.")
            else:
                messages.info(request, f'Your review has been successfully modified.')
            return render(request, 'review_form.html', {'form': form, 'book_id': book.id})
    return render(request, 'review_form.html', {'form': form, 'book_id': book.id})

