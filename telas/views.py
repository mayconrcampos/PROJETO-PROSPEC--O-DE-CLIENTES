from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, "dashboard.html")

def perfis(request):
    return render(request, 'perfis/perfis.html')

def configuracoes(request):
    return render(request, "configuracoes.html")

def clientes(request):
    return render(request, "clientes.html")

def estoque(request):
    return render(request, "estoque.html")

def vendas(request):
    return render(request, "vendas.html")