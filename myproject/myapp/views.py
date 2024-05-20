from django.shortcuts import render
from . import models

def index(request):
    items=models.TodoItem.objects.all()
    return render(request, '1.html' , {'items':items})

def aboutme(request):
    return render(request, 'aboutme.html')