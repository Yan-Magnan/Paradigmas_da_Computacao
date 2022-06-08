from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'sobre_nos.html')


def cardapio(request):
    return HttpResponse('cardapio 1')


def contato(request):
    return HttpResponse('contato 1')


def endereco(request):
    return HttpResponse('endereco 1')