from django.shortcuts import render
from django.http import HttpResponse

def view(request):
    return HttpResponse('<h1 style="text-align: center; background-color: yellow">Домашка по 4 уроку</h1>')