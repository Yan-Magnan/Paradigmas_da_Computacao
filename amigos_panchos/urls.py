from django.urls import path

from amigos_panchos import views

urlpatterns = [
    path('', views.home, name='sobre-nos'),
    path('cardapio/', views.cardapio, name='cardapio'),
    path('contato/', views.contato, name='contato'),
    path('endereco/', views.endereco, name='endereco'),
    # path('login/', views.login, name='login'),
    # path('cadastro/', views.cadastro, name='cadastro'),




    path('informacao/pancho/<str:pancho_nome>', views.informacao, name='informacao'),
    path('informacao/burguer/<str:burguer_nome>', views.informacao_burguer, name='informacao_burguer'),
    path('informacao/xis/<str:xi_nome>', views.informacao_xis, name='informacao_xis'),
    path('informacao/fritas/<str:frita_nome>', views.informacao_fritas, name='informacao_fritas'),
    path('informacao/bebidas/<str:bebida_nome>', views.informacao_bebidas, name='informacao_bebidas'),

    # path('', home),

]
