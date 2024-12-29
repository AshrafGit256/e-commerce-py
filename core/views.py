from django.shortcuts import render
from django.http import HttpResponse  # Import HttpResponse

def index(request):
    return render(request, 'core/index.html')
