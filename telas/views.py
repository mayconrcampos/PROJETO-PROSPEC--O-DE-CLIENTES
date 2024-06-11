from django.shortcuts import render, redirect
from .services import TelaServices
from .decorators import login_requerido

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    print("chegay aq    ui")
    logado = TelaServices.login(request=request)
    return redirect("dashboard") if logado else redirect("index")

def logout(request):
    deslogado = TelaServices.logout(request=request)
    return redirect("index") if deslogado else redirect("dashboard")

@login_requerido
def dashboard(request):
    return render(request, "dashboard.html")

@login_requerido
def cadastros(request):
    return render(request, 'perfis/cadastros.html')

@login_requerido
def empresas(request):
    context = TelaServices.obtem_empresas(request=request)
    return render(request, "perfis/empresa.html", context)

@login_requerido
def cadastra_empresa(request):
    TelaServices.cadastra_empresa(request=request)
    return redirect("empresas")

@login_requerido
def atualiza_empresa(request):
    TelaServices.atualiza_empresa(request=request)
    return redirect("empresas")

@login_requerido
def excluir_empresa(request):
    TelaServices.excluir_empresa(request=request)
    return redirect("empresas")

# def configuracoes(request):
#     return render(request, "configuracoes.html")

# def clientes(request):
#     return render(request, "clientes.html")

# def estoque(request):
#     return render(request, "estoque.html")

# def vendas(request):
#     return render(request, "vendas.html")