from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def hello(request):
#     text = '<h1>Hello World!</h1>'
#     return HttpResponse(text)

def hello(request):
    return render(request, 'test_app/hello.html')
