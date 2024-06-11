from django.urls import path
from .views import index, login, logout, dashboard, cadastros, empresas, cadastra_empresa, atualiza_empresa, excluir_empresa#, configuracoes, clientes, estoque, vendas

urlpatterns = [
    path("", index, name='index'),
    path("login", login, name='login'),
    path("logout", logout, name='logout'),
    path("app/dashboard", dashboard, name='dashboard'),
    path("app/cadastros", cadastros, name='cadastros'),
    path("app/cadastros/empresas", empresas, name='empresas'),
    path("app/cadastros/cadastra/empresa", cadastra_empresa, name='cadastra_empresa'),
    path("app/cadastros/atualiza/empresa", atualiza_empresa, name='atualiza_empresa'),
    path("app/cadastros/excluir/empresa", excluir_empresa, name='excluir_empresa'),

]