from django.http import HttpResponse
from django.shortcuts import render
from .models import NewPost


def index(request):
    news = NewPost.objects.all()

    return render(request, "index.html", {'news':news})

def page(request, id):
    post = NewPost.objects.get(id = id)
    post.views+= 1
    post.save(update_fields=['views'])
    return render(request, "page.html", {'post':post})

def tags(request, name):
    posts = NewPost.objects.all()
    return render(request, "tags.html", {'keyword':name, 'post':posts})

def stat(request):
    news = NewPost.objects.all()

    return render(request, "stat.html", {'news':news})