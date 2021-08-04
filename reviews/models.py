from django.db import models
from django.contrib import auth
from books.models import Book
# Create your models here.


class ReviewBook(models.Model):
    review_id = models.IntegerField(primary_key=True, editable=False)
    content = models.TextField(help_text='The review text.')
    rating = models.IntegerField(help_text='The rating the reviewer has given')
    created_at = models.DateTimeField(auto_now_add=True, help_text='The date and time the review was created',
                                      editable=False)
    edited_at = models.DateTimeField(null=True, help_text='The date and time the review was edited for the last time',
                                     editable=False)
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, editable=False, on_delete=models.CASCADE, help_text='The book the review for')

