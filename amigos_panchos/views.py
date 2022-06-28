from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from amigos_panchos.models import cadastroCliente


def home(request):
    return render(request, 'pages/sobre_nos.html')


def cardapio(request):
    return render(request, 'pages/cardapio.html')


def contato(request):
    return render(request, 'pages/contato.html')


def endereco(request):
    return render(request, 'pages/enderecos.html')


def login(request):
    return render(request, 'pages/login.html')


def cadastro(request):
    nome = request.POST.get('nome')
    telefone = request.POST.get('telefone')
    dataNascimento = request.POST.get('dataNascimento')
    cep = request.POST.get('cep')
    senha1 = request.POST.get('senha1')
    rua = request.POST.get('rua')
    numero = request.POST.get('numero')
    bairro = request.POST.get('bairro')
    cidade = request.POST.get('cidade')
    senha2 = request.POST.get('senha2')

    return redirect('login')
