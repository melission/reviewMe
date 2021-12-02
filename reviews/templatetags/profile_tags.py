from reviews.models import ReviewBook
from books.models import Book
from django import template
from django.db.models import Q


register = template.Library()


@register.inclusion_tag('reviews_list.html')
def reviews_list_tag(user_id):
    # print(user_id)
    raw_reviews = ReviewBook.objects.filter(creator_id=user_id)
    reviews = []
    if len(raw_reviews) > 0:
        for review in raw_reviews:
            book = Book.objects.get(id=review.book_id)
            contributors = book.contributors.filter(
                Q(bookcontributor__role='AUTHOR') | Q(bookcontributor__role='CO_AUTHOR')
            )
            reviews.append(
                {
                    'content': review.content,
                    'rating': review.rating,
                    'authors': contributors,
                    # 'created_at': review.created_at.date(),
                    'book_id': review.book.id,
                    'book_title': review.book.title,

                }
            )
    # print(reviews)
        return {"reviews": reviews}
    else:
        return None

