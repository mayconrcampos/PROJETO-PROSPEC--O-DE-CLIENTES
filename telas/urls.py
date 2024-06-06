from django.urls import path
from .views import index, dashboard, perfis, configuracoes, clientes, estoque, vendas

urlpatterns = [
    path("", index, name='index'),
    path("app/dashboard", dashboard, name='dashboard'),
    path("app/perfis", perfis, name='perfis'),
    path("app/configuracoes", configuracoes, name='configuracoes'),
    path("app/clientes", clientes, name='clientes'),
    path("app/estoque", estoque, name='estoque'),
    path("app/vendas", vendas, name='vendas'),
]