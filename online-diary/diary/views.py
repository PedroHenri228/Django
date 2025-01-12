from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'home.html')

def escrever(request):
    
    if request.method == 'GET':
        
        return render(request, 'escrever.html')
    
    elif request.method == 'POST':
        
        titulo = request.POST['titulo']
        tags = request.POST['tags']
        pessoas = request.POST['pessoas']
        texto = request.POST['texto']
        
        
        
        return HttpResponse(f'Título => {titulo}, Tags => {tags}, Pessoas => {pessoas}, Texto => {texto}')
    
        