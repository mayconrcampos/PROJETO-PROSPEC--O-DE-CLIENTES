from django.urls import path
from .views import prospeccoes, registros, registrar_prospeccao, htmx_registros

urlpatterns = [
    path("app/prospeccoes", prospeccoes, name="prospeccoes"),
    path("app/prospeccoes/registros", registros, name="registros"),
    path("app/prospeccoes/htmx/registros", htmx_registros, name="htmx_registros"),
    path("app/prospeccoes/htmx/registros/<str:page>", htmx_registros, name="htmx_registros"),
    path("app/prospeccoes/registrar/prospeccao", registrar_prospeccao, name="registrar_prospeccao"),
]