from django.http import HttpResponse
from django.shortcuts import render
from amigos_panchos.models import Categoria, Pancho, Burguer, Frita, Bebida, Xi, Sobre


#############################################################   Bebidas ver mais
def informacao_bebidas(request, bebida_nome):
    categoria = Categoria.objects.all()
    bebida = Bebida.objects.get(nome=bebida_nome)

    return render(request, 'pages/informacao_lanche.html', {
        'categoria' : categoria,
        'bebida': bebida,

    })


#############################################################   Fritas ver mais
def informacao_fritas(request, frita_nome):
    categoria = Categoria.objects.all()
    frita = Frita.objects.get(nome=frita_nome)

    return render(request, 'pages/informacao_lanche.html', {
        'categoria' : categoria,
        'frita': frita,

    })



#############################################################xis ver mais
def informacao_xis(request, xi_nome):
    categoria = Categoria.objects.all()

    xi = Xi.objects.get(nome=xi_nome)

    return render(request, 'pages/informacao_lanche.html', {
        'categoria' : categoria,
        'xi': xi,
    })


##############################################################Burguer ver mais

def informacao_burguer(request, burguer_nome):
    categoria = Categoria.objects.all()
    burguer = Burguer.objects.get(nome=burguer_nome)

    return render(request, 'pages/informacao_lanche.html', {
        'categoria' : categoria,
        'burguer': burguer,

    })


#############################################################Pancho ver mais
def informacao(request, pancho_nome):
    categoria = Categoria.objects.all()
    burguer = Burguer.objects.all()
    frita = Frita.objects.all()
    bebida = Bebida.objects.all()
    xi = Xi.objects.all()

    pancho = Pancho.objects.get(nome=pancho_nome)
    return render(request, 'pages/informacao_lanche.html', {
        'categoria' : categoria,
        'pancho': pancho,
        'burguer': burguer,
        'xi': xi,
        'frita': frita,
        'bebida': bebida,
    })


def home(request):
    sobre = Sobre.objects.all()
    return render(request, 'pages/sobre_nos.html',{
        'sobre':sobre
    })


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


# def login(request):
#     return render(request, 'pages/login.html')
#
#
# def cadastro(request):
#     return render(request, 'pages/cadastro.html')
