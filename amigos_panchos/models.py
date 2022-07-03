from tkinter import CASCADE

from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

####                                                                            Pancho
class Pancho(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=1000)
    preco = models.CharField(max_length=255)
    link = models.CharField(max_length=800)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m')

    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome


####                                                                            Burguer

class Burguer(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=1000)
    preco = models.CharField(max_length=255)
    link = models.CharField(max_length=800)
    foto = models.ImageField(blank=True, upload_to='fotosBurguer/%Y/%m')


    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome


####                                                                            Fritas
class Frita(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=1000)
    preco = models.CharField(max_length=255)
    link = models.CharField(max_length=800)
    foto = models.ImageField(blank=True, upload_to='fotosFritas/%Y/%m')


    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome

####                                                                            Bebidas
class Bebida(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=1000)
    preco = models.CharField(max_length=255)
    link = models.CharField(max_length=800)
    foto = models.ImageField(blank=True, upload_to='fotosBebidas/%Y/%m')


    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome

####                                                                            XIS

class Xi(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=1000)
    preco = models.CharField(max_length=255)
    link = models.CharField(max_length=800)
    foto = models.ImageField(blank=True, upload_to='fotosXis/%Y/%m')


    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome


####                                                                            Aba sobre

class Sobre(models.Model):
    descricao = models.TextField(max_length=1200)
    foto = models.ImageField(blank=True, upload_to='fotosSobre/%Y/%m')

    def __str__(self):
        return self.descricao
