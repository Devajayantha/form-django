from django.shortcuts import render, redirect
from blog import models, forms
from django.http import HttpResponse, Http404
# Create your views here.

def index(request):
    return render(request, 'blog/index.html',{
        'tittle': 'My Blog',
        'content' : models.Post.objects.all

    })

def detail(request, id):
    try:
        model = models.Post.objects.get(id=id)
    except Exception:
        raise Http404()
    form = forms.CommentForm(request.POST if request.method == 'POST' else {'post':model})
    if form.is_valid():
        # .save() masuk kedatabase
        form.save()
        return  redirect('blog-detail',id=id)
    return render(request, 'blog/detail.html',{
        'title':model.title,
        'model_baru':model,
        'form':form
    })

