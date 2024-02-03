from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Pessoa

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro/index.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        pessoa = Pessoa(
            nome = nome,
            email = email,
            senha = senha
        )
        pessoa.save()
        return HttpResponse('Cadastro efetuado com sucesso!')
    

def listar(request):
    
    dados = Pessoa.objects.filter(nome='Guilherme').filter(senha=123456)[0] # primeiro filtrar para depois atualizar. Utilizar [0] porque sempre retorna uma lista mesmo sendo um dado só
    dados.nome = 'Guilherme Montenegro'
    dados.save()
    
    pessoas = Pessoa.objects.all()
    return render(request, 'listar/listar.html', {'pessoas': pessoas})
    
 