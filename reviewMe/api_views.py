from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.pagination import LimitOffsetPagination
from books.models import *
from movies.models import *
from reviews.models import ReviewBook
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView

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

class Login(APIView):

    # the default "POST" method is to be overwritten, so it will be able t provide a used with a token,
    # which can be used in lieu of entering 'username' and 'password'. [security measures]
    def post(self, request):
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if not user:
            return Response({'error': "User doesnt' exist, or credentials are incorrect"}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)


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

