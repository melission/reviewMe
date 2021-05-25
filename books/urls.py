from django.urls import path
from .views import *

urlpatterns = [
    # path('', books_all),
    path('', BookHomePage.as_view()),
    path('search/', book_search),
]