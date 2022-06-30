from tkinter import CASCADE

from django.db import models


class Panchos(models.Model):
    nome = models.CharField("nome", max_length=200)
    descrição = models.TextField("descrição", blank=True)
    preço = models.CharField("preço", max_length=100)
    imagem = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.nome


class Burguer(models.Model):
    nome = models.CharField("nome", max_length=200)
    descrição = models.TextField("descrição", blank=True)
    preço = models.CharField("preço", max_length=100)
    imagem = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.nome


class Fritas(models.Model):
    nome = models.CharField("nome", max_length=200)
    descrição = models.TextField("descrição", blank=True)
    preço = models.CharField("preço", max_length=100)
    imagem = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.nome


class Bebidas(models.Model):
    nome = models.CharField("nome", max_length=200)
    descrição = models.TextField("descrição", blank=True)
    preço = models.CharField("preço", max_length=100)
    imagem = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.nome
