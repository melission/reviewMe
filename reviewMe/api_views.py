from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.pagination import LimitOffsetPagination
from books.models import *
from movies.models import *
from reviews.models import ReviewBook
from .serializers import *

# @api_view()
# def all_books(request):
#     books = Book.objects.all()
#     book_serializer = BookSerializer(books, many=True)
#     return Response(book_serializer.data)


# class AllBooks(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class ContributorView(generics.ListAPIView):
#     queryset = Contributor.objects.all()
#     serializer_class = ContributorSerializer

class AllBookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReviewBookViewSet(viewsets.ModelViewSet):
    queryset = ReviewBook.objects.order_by('-created_at')
    serializer_class = ReviewBookSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = []


class AllMovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

