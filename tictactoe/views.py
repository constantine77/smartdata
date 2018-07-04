from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return HttpResponse("TIC TAC TOE!!!")

def index(request):
    return render(request, 'index.html')


