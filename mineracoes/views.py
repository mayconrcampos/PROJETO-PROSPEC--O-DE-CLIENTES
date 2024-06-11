from django.shortcuts import render, redirect
from .services import MineracoeServices

# Create your views here.
def mineracao(request):
    return render(request, "mineracao.html")

def subir_arquivo(request):
    MineracoeServices.subir_arquivo(request=request)
    return redirect('mineracao')