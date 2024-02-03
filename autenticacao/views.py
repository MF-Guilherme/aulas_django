from django.shortcuts import render
from django.http import HttpResponse
import json

def cadastro(request):
    # exemplo de URL: http://127.0.0.1:8000/autenticacao/cadastro/?nome=Guilherme&sobrenome=Montenegro&idade=32
    
    # pegando dados da url pelo parâmetro request
    nome = request.GET.get('nome')
    sobrenome = request.GET.get('sobrenome')
    idade = request.GET.get('idade')
    return render(request, 'cadastro/index.html', {'nome': nome, 'sobrenome': sobrenome, 'idade': idade})


def valida_formulario(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    return HttpResponse(json.dumps({'nome': nome, 'email': email})) 