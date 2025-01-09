from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return HttpResponse("hey")