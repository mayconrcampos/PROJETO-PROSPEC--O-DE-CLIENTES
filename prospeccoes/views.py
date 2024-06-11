from django.shortcuts import render, redirect
from .services import ProspeccoeServices

# Create your views here.
def prospeccoes(request):
    return render(request, "prospeccoes.html")

def registros(request):
    context = ProspeccoeServices.obter_prospeccoes(request=request)
    return render(request, "registros.html", context)

def registrar_prospeccao(request):
    page = ProspeccoeServices.registrar_prospeccao(request=request)
    print("page ", page)
    return redirect('htmx_registros', page)

def htmx_registros(request, page=None):
    context = ProspeccoeServices.obter_prospeccoes(request=request, page=page)
    return render(request, "htmx_registros.html", context)

