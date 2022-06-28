from tkinter import CASCADE

from django.contrib.auth.models import User
from django.db import models


class cadastroCliente(models.Model):

    user = models.OneToOneField(User, null=True,  on_delete=models.CASCADE)
    nome = models.CharField("nome", max_length=200)
    telefone = models.CharField("telefone", max_length=200)
    dataNascimento = models.CharField("dataNascimento", max_length=200)
    cep = models.CharField("cep", max_length=200)
    senha1 = models.CharField("senha1", max_length=200)
    rua = models.CharField("rua", max_length=200)
    numero = models.CharField("numero", max_length=200)
    bairro = models.CharField("bairro", max_length=200)
    cidade = models.CharField("cidade", max_length=200)
    senha2 = models.CharField("senha2", max_length=200)

    @ staticmethod
    def cria_cliente(nome, telefone, dataNascimento, cep, senha1, rua, numero, bairro, cidade, senha2):
        criacao = cadastroCliente.objects.create(
            nome=nome, telefone=telefone, dataNascimento=dataNascimento, cep=cep, senha1=senha1, rua=rua, numero=numero, bairro=bairro, cidade=cidade, senha2=senha2
        )
        criacao.save()

    def __str__(self):
        return self.nome
