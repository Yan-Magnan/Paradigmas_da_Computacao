from django.urls import path

from amigos_panchos import views

urlpatterns = [
    path('', views.home, name='sobre-nos'),
    path('cardapio/', views.cardapio, name='cardapio'),
    path('contato/', views.contato, name='contato'),
    path('endereco/', views.endereco, name='endereco'),
    # path('', home),

]
