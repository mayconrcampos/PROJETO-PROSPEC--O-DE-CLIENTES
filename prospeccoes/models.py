from django.db import models
from telas.models import Empresa, Base
# Create your models here.
class Prospeccao(Base):
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE, blank=False)
    msg_enviada = models.BooleanField("Mensagem Enviada?", default=False)
    cliente_respondeu = models.BooleanField("Cliente respondeu?", default=False)
    indicado = models.BooleanField("Foi indicado?", default=False)
    comentarios = models.TextField("Comentarios", default="")

    class Meta:
        verbose_name = "Prospecçõe"

    def __str__(self):
        return self.empresa.razao_social