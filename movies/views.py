from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def movies_all(request):
    return HttpResponse('Movies will be here someday')