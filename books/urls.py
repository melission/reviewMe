from django.urls import path
from .views import books_all

urlpatterns = [
    path('', books_all)
]