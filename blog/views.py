from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    

    posts = Post.objects.all()
    cats = Category.objects.all()
    data = {'posts': posts , 'cats' : cats}
    
    return render(request , 'home.html' , data)

def post(request , url):
    queryset = Post.objects.get(url = url)
    cats = Category.objects.all()
    
    return render(request , 'posts.html' , {'queryset' : queryset ,'cats' : cats})

def display_post(request , url):

    cat = Category.objects.get(url = url)
    post = Post.objects.filter(cat = cat)

    return render(request , 'category_posts.html' , { 'cat' : cat , 'post' : post})