from django.urls import path
from .views import *


urlpatterns = [
    path('', movies_all),
    path('<int:id>/', detailed_movie),
]