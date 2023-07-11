from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1 style="text-align: center; background-color: yellow">Всё ок!</h1>')