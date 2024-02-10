from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Pessoa, Cargo
from django.http import Http404
from django.shortcuts import get_list_or_404

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
    pessoas = Pessoa.objects.all()
    return render(request, 'listar/listar.html', {'pessoas': pessoas})

def listar_unico(request, id):
    # LANÇANDO 404 DE UMA FORMA:
    # pessoa = Pessoa.objects.filter(id = id)    
    # if len(pessoa) == 0:
    #     raise Http404('Esta pessoa não existe')
    
    # LANÇANDO 404 DE OUTRA FORMA:
    pessoa = get_list_or_404(Pessoa, id = id)
    return render(request, 'listar/listar.html', {'pessoas': pessoa})
    
