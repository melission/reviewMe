from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer

# @api_view()
# def all_books(request):
#     books = Book.objects.all()
#     book_serializer = BookSerializer(books, many=True)
#     return Response(book_serializer.data)


class AllBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
