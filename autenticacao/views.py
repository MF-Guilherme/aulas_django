from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    pessoa = [{'nome': 'Guilherme Montenegro',
              'idade': '20',
              'profissao': 'Programador'},
              
              {'nome': 'Isaac Montenegro',
              'idade': '1',
              'profissao': 'Programador'}]
    return render(request, 'cadastro/index.html', {'pessoas': pessoa, 'x': 0})


def login(request):
    return render(request, 'login/index.html')


def auth(request):
    return HttpResponse('Url vazia')