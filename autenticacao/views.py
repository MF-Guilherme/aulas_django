from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    nome = 'Guilherme Montenegro'
    idade = '20'
    profissao = 'Programador'
    return render(request, 'cadastro/index.html', {'nome': nome, 'idade': idade, 'profissao': profissao})


def login(request):
    return render(request, 'login/index.html')


def auth(request):
    return HttpResponse('Url vazia')