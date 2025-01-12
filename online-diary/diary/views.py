from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa, Diario
# Create your views here.


def home(request):
    return render(request, 'home.html')

def escrever(request):
    
    if request.method == 'GET':
        
        pessoas = Pessoa.objects.all()
        return render(request, 'escrever.html', {'pessoas': pessoas})
    
    elif request.method == 'POST':
        
        titulo = request.POST['titulo']
        tags = request.POST['tags']
        pessoas = request.POST['pessoas']
        texto = request.POST['texto']
        
        if len(titulo.strip()) == 0 or len(texto.strip()) == 0:
            
            return redirect('escrever')
        
        diario = Diario(
            titulo=titulo,
            texto=texto
        )
        
        diario.set_tags(tags)
        diario.save()
        
        for i in pessoas:
            pessoa = Pessoa.objects.get(id=i)
            diario.pessoas.add(pessoa)
        
        diario.save()
        return redirect('escrever')
    

def cadastrar_pessoa(request):
    
    if request.method == 'GET':
        
        return render(request, 'pessoa.html')
    
    elif request.method == 'POST':
        
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')

        pessoa = Pessoa(
            nome=nome,
            foto=foto
        )
        pessoa.save()
        return redirect('escrever')
    