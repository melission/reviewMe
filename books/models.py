from django.db import models
from django.contrib import auth

# from books.models import Contributor, Book, Publisher, BookContributor, Review
# Create your models here.


class Publisher(models.Model):
    """The company that publishing books.
    One to many relationship."""
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=64)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Many to many relationship. A book can be written by several contributors.
    A contributor can [help] create several books"""
    id = models.IntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=64,
                             help_text='The title of the book', blank=False)
    # cover = models.ImageFiled()
    published_at = models.DateTimeField(help_text='The year the book was published')
    # publisher_name = models.CharField(max_length=64, help_text='Publisher name')
    description = models.CharField(max_length=1000)
    review = models.TextField
    isbn = models.CharField(max_length=13, verbose_name='ISBN number of the book')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through='BookContributor')

    # def isnb_with_dashes(self):
    #     """ '9780316769174' => '978-0-31-676917-4' """
    #     return '{}-{}-{}-{}-{}'.format(
    #         self.isbn[0:3], self.isbn[3:4], self.isbn[4:6], self.isbn[6:12], self.isbn[12:13])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/books/details/%i/" % self.id


class Contributor(models.Model):
    """A contributor to a Book. Author, editor, etc.
    Many to many relationship (a contributor may create several books, a book can be written by several contributors"""
    id = models.IntegerField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# the model helps to save data to both tables: Book and Contributor
class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = 'AUTHOR', 'Author'
        CO_AUTHOR = 'CO_AUTHOR', 'Co-Author'
        EDITOR = 'EDITOR', 'Editor'
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name='The role that a contributor had in the book',
                            choices=ContributionRole.choices,
                            max_length=20)

    def __str__(self):
        return f'{self.book} {self.contributor} {self.role}'


class Review(models.Model):
    content = models.TextField(help_text='The review text.')
    rating = models.IntegerField(help_text='The rating the reviewer has given')
    created_at = models.DateTimeField(auto_now_add=True, help_text='The date and time the review was created',
                                      editable=False)
    edited_at = models.DateTimeField(null=True, help_text='The date and time the review was edited for the last time',
                                     editable=False)
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text='The book the review for')
