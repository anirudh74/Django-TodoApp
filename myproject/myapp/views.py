from django.shortcuts import render, redirect
from . import models

def index(request):
    items=models.TodoItem.objects.all()
    return render(request, '1.html' , {'items':items})

def aboutme(request):
    return render(request, 'aboutme.html')

def complete(request,id):
    item=models.TodoItem.objects.get(pk=id)
    item.status = True
    item.save()
    return redirect('index')

def delete(request,id):
    item=models.TodoItem.objects.get(pk=id)
    item.delete()
    return redirect('index')

def add(request):
    if request.method=='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        models.TodoItem.objects.create(title=title,description=description,created_at=date)
    return redirect('index')