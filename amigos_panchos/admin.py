from django.contrib import admin

from amigos_panchos.models import User, cadastroCliente


@admin.register(cadastroCliente)
class cadastroClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "senha1", "cidade", "telefone")
