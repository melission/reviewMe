from django.urls import path
from .views import *

urlpatterns = [
    # path('', books_all),
    path('', BookHomePage),
    path('search/', book_search),
]