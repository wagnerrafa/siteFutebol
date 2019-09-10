from django.shortcuts import render
from home.models import Post, Marcar_Jogo

# Create your views here.

def home(request):
    noticias = Post.objects.all()
    noticia = Marcar_Jogo.objects.all()
    noti = Marcar_Jogo.objects.all()
    contexto = ''
    vitoria = 0
    derrota = 0
    empate = 0
    for re in noti:
            if re.placarCasa == None:
                break
            if re.placarCasa > re.placarFora:
                vitoria = vitoria+1
            elif re.placarCasa < re.placarFora:
                derrota = derrota+1
            else: empate = empate+1
    

    if request.method == 'POST':
        pessoa = Marcar_Jogo()
        pessoa.name = request.POST['name']
        pessoa.time = request.POST['time']
        pessoa.end = request.POST['end']
        pessoa.tel = request.POST['tel']
        pessoa.email = request.POST['email']
        pessoa.date = request.POST['date']
        pessoa.lugar = request.POST['lugar']
        pessoa.msg = request.POST['msg']                 
        contexto = 'Pedido de contra recebido, em breve confirmaremos o jogo'

        
        pessoa.save()

    return render(request, 'index.html', {'msgOk': contexto,'posts': noticias, 'resultado':noticia,'msgRe': noti,'reVit': vitoria,'reEmpa': empate,'reDer': derrota})

def resultado(request):
    resultado_placar = Marcar_Jogo.objects.all()
    
    
    if request.method =='POST':
        placa = Marcar_Jogo()
        placa.placarCasa = request.POST['reCasa']
        placa.placarFora = request.POST['reFora']
        placa.save()
        
    return render(request, 'resultado.html', {'msgRe':resultado_placar})