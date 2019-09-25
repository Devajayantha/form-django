from django.shortcuts import render
from blog import models
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'blog/index.html',{
        'tittle': 'My Blog',
        'content' : models.Post.objects.all

    })

def detail(request, id):
    model = models.Post.objects.get(id=id)
    return render(request, 'blog/detail.html',{
        'title':model.title,
        'model':model
    })

