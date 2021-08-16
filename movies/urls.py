from django.urls import path
from .views import *


urlpatterns = [
    path('', movies_all),
    path('details/<int:id>/', detailed_movie),
    path('add_person/', add_person)
]