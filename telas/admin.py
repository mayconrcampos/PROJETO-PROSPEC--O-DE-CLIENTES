from django.contrib import admin
from .models import Empresa
# Register your models here.

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = (
        "razao_social",
        "cnpj",
        "ramo",
        "email",
        "fone",
        "tem_zap",
        "cnae_principal",
        "cnae_secundario",
        "bairro",
        "cidade",
        "uf"
    )