from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'pages/sobre_nos.html')


def cardapio(request):
    return render(request, 'pages/cardapio.html')


def contato(request):
    return render(request, 'pages/contato.html')


def endereco(request):
    return render(request, 'pages/enderecos.html')
