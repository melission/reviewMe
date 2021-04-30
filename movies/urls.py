from django.urls import path
from .views import movies_all


urlpatterns = [
    path('', movies_all)
]