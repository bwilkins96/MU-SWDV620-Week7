# SWDV 620: Web Applications
# Django views

from django.shortcuts import render

def index(request):
    return render(request, 'endpoints/index.html')

def view_1(request):
    return render(request, 'endpoints/view_1.html')

def view_2(request):
    context = {'message': 'Hello from the view_2 function!'}
    return render(request, 'endpoints/view_2.html', context)
