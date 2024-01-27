from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return render(request, 'cadastro/index.html')


def login(request):
    return render(request, 'login/index.html')


def auth(request):
    return HttpResponse('Url vazia')