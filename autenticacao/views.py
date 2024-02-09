from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Pessoa, Cargo

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
    # CADASTRANDO USUÁRIOS COM DADOS PASSADOS PELA URL:

    # if len(request.GET) != 0:
    #     nome = request.GET.get('nome')
    #     email = request.GET.get('email')
    #     senha = request.GET.get('senha')

    #     cargo = Cargo.objects.get(id=1)

    #     pessoa = Pessoa(nome=nome,
    #                     email=email,
    #                     senha=senha,
    #                     cargo=cargo)

    #     pessoa.save()

    # FILTRANDO PELO CARGO
    # cargo = Cargo.objects.get(id = 1)
    # pessoas = Pessoa.objects.filter(cargo = cargo)
    # pessoas = Pessoa.objects.filter(cargo__pk = 1) # uma opção diferente que funciona da mesma formas
    
    # ALTERANDO O CARGO
    cargo = Cargo.objects.get(id = 1)
    pessoa = Pessoa.objects.get(id = 2)
    pessoa.cargo = cargo
    pessoa.save()
        
    pessoas = Pessoa.objects.all()
    return render(request, 'listar/listar.html', {'pessoas': pessoas})
