from django.urls import path
from .views import *
from reviews.views import book_list_page

urlpatterns = [
    path('', books_all),
    # path('', BookHomePage.as_view()),
    path('search/', book_search),
    path('rating/', book_list_page)
]