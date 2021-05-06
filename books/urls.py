from django.urls import path
from .views import *

urlpatterns = [
    path('', books_all),
    path('search/', book_search),
]