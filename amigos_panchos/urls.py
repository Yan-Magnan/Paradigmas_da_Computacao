from django.urls import path
from amigos_panchos.views import home, cardapio, contato, endereco


urlpatterns = [
    path('', home),
    path('cardapio/', cardapio),
    path('contato/', contato),
    path('endereco/', endereco),
    # path('', home),

]