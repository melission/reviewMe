from reviews.models import ReviewBook
from django import template

register = template.Library()


@register.inclusion_tag('reviews_list.html')
def reviews_list_tag(user_id):
    # print(user_id)
    raw_reviews = ReviewBook.objects.filter(creator_id=user_id)
    reviews = []
    for review in raw_reviews:
        reviews.append(
            {
                'content': review.content,
                'rating': review.rating,
                # 'created_at': review.created_at.date(),
                'book_id': review.book.id,
                'book_title': review.book.title,

            }
        )
    # print(reviews)
    return {"reviews": reviews}
