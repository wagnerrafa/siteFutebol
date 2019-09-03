from django.shortcuts import render
from home.models import Post

# Create your views here.

def home(request):
    noticias = Post.objects.all()

    return render(request, 'index.html', {'posts': noticias})

def viewBlog(request, post_id):
    noticia = Post.objects.get(pk=post_id)
    lastNews = Post.objects.all()

    return render(request, 'index.html', {'post': noticia, 'blogPosts': lastNews})