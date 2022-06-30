from django.contrib import admin

from amigos_panchos.models import Bebidas, Burguer, Fritas, Panchos


@admin.register(Panchos)
class PanchosAdmin(admin.ModelAdmin):
    list_display = ("nome", "preço", "imagem")


@admin.register(Burguer)
class BurguerAdmin(admin.ModelAdmin):
    list_display = ("nome", "preço", "imagem")


@admin.register(Fritas)
class Fritas(admin.ModelAdmin):
    list_display = ("nome", "preço", "imagem")


@admin.register(Bebidas)
class BebidasAdmin(admin.ModelAdmin):
    list_display = ("nome", "preço", "imagem")
