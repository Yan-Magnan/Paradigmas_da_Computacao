from django.contrib import admin

from amigos_panchos.models import Categoria, Pancho, Burguer, Frita, Bebida, Xi


admin.site.register(Categoria)

####                                                                            Pancho
@admin.register(Pancho)
class PanchoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao", "preco", "link", "categoria")
    list_filter = ("nome", "preco")
    list_per_page = 10
    search_fields = ("nome", "preco", "categoria")


####                                                                            Burguer
@admin.register(Burguer)
class BurguerAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao", "preco", "link", "categoria")
    list_filter = ("nome", "preco")
    list_per_page = 10
    search_fields = ("nome", "preco", "categoria")


####                                                                            Xis
@admin.register(Xi)
class XiAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao", "preco", "link", "categoria")
    list_filter = ("nome", "preco")
    list_per_page = 10
    search_fields = ("nome", "preco", "categoria")


####                                                                            Frintas
@admin.register(Frita)
class FritaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao", "preco", "link", "categoria")
    list_filter = ("nome", "preco")
    list_per_page = 10
    search_fields = ("nome", "preco", "categoria")


####                                                                            Bebidas
@admin.register(Bebida)
class BebidaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao", "preco", "link", "categoria")
    list_filter = ("nome", "preco")
    list_per_page = 10
    search_fields = ("nome", "preco", "categoria")