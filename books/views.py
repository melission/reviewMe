from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def books_all(request):
    return HttpResponse('Books list')