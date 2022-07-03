from django.http import HttpResponse
from django.shortcuts import render
from amigos_panchos.models import Categoria, Pancho, Burguer, Frita, Bebida, Xi



def home(request):
    return render(request, 'pages/sobre_nos.html')


def cardapio(request):
    categoria = Categoria.objects.all()
    burguer = Burguer.objects.all()
    frita = Frita.objects.all()
    bebida = Bebida.objects.all()
    xi = Xi.objects.all()

    panchos = Pancho.objects.all()
    return render(request, 'pages/cardapio.html', {
        'categorias' : categoria,
        'panchos': panchos,
        'burguers': burguer,
        'xis': xi,
        'fritas': frita,
        'bebidas': bebida,


    })


def contato(request):
    return render(request, 'pages/contato.html')


def endereco(request):
    return render(request, 'pages/enderecos.html')


def login(request):
    return render(request, 'pages/login.html')


def cadastro(request):
    return render(request, 'pages/cadastro.html')
