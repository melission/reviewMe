from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # http://127.0.0.1:8000/?name=True shows True page
    # http://127.0.0.1:8000/?name=    [with spaces] is being considered as an empty str
    # http://127.0.0.1:8000/?name='       ' turned out as name=''
    name = request.GET.get("name") or "index"
    # return HttpResponse(f'{name} page')
    return render(request, 'index.html', {'name': name})
