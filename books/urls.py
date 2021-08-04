from django.urls import path
from .views import *
from reviews.views import book_review_edit

urlpatterns = [
    # path('', books_all),
    # path('', BookHomePage.as_view()),
    # path('search/', book_search),
    # path('rating/', book_list_page),
    path('', book_list_page),
    path('rating/', book_list_page),
    path('details/<int:id>/', detailed_book_view),
    path('details/<int:id>/add_review/', book_review_edit),
    path('publishers/<int:p_id>/', publisher_edit, name='publisher_edit'),
    path('publishers/new/', publisher_edit, name='publisher_create'),
]
