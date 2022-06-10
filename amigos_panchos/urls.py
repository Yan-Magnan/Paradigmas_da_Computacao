from django.urls import path

from amigos_panchos import views

urlpatterns = [
    path('', views.home),
    path('cardapio/', views.cardapio),
    path('contato/', views.contato),
    path('endereco/', views.endereco),
    # path('', home),

]
