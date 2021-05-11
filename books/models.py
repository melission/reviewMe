from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64,
                             help_text='The title of the book', blank=False)
    # cover = models.ImageFiled()
    published_at = models.IntegerField(help_text='The year the book was published')
    publisher_name = models.CharField(max_length=64, help_text='Publisher name')
    description = models.CharField(max_length=1000)
    review = models.TextField
    isbn - models.CharField(max_length=20, verbose_name='ISBN number of the book')



