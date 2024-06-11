from django.contrib import admin
from .models import Prospeccao
# Register your models here.

@admin.register(Prospeccao)
class ProspeccaoAdmin(admin.ModelAdmin):
    list_display = ("empresa", "msg_enviada", "cliente_respondeu", "indicado")
