from django.shortcuts import render
from home.models import Post, Marcar_Jogo

# Create your views here.

def home(request):
    noticias = Post.objects.all()
    noticia = Marcar_Jogo.objects.all()
    if request.method == 'POST':
        pessoa = Marcar_Jogo()
        pessoa.name = request.POST['name']
        pessoa.time = request.POST['time']
        pessoa.end = request.POST['end']
        pessoa.tel = request.POST['tel']
        pessoa.email = request.POST['email']
        pessoa.date = request.POST['date']
        pessoa.hora = request.POST['hora']
        pessoa.lugar = request.POST['lugar']
        pessoa.msg = request.POST['msg']
        pessoa.save()
    return render(request, 'index.html', {'posts': noticias},{'time': noticia})