from django.shortcuts import render
from home.models import Post

# Create your views here.

def home(request):
    noticias = Post.objects.all()

    return render(request, 'index.html', {'posts': noticias})