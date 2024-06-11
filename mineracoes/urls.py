from django.urls import path
from . import views


urlpatterns = [
    path("app/mineracao", views.mineracao, name="mineracao"),
    path("app/mineracao/subir-arquivo", views.subir_arquivo, name="subir_arquivo"),
]