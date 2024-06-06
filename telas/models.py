from django.db import models

# Create your models here.
class Base(models.Model):
    criado = models.DateTimeField("Criado", auto_now_add=True)
    modificado = models.DateTimeField("Modificado", auto_now=True)
    ativo = models.BooleanField("Ativo?", default=True)

    class Meta:
        abstract = True

class Empresa(Base):
    razao_social = models.CharField("Razão Social", max_length=256, blank=False)
    cnpj = models.CharField("CNPJ", unique=True, max_length=18, blank=False)
    ramo = models.CharField("Ramo de Atuação", max_length=128, blank=False)
    email = models.EmailField("Email", unique=True, blank=False)
    fone = models.CharField("fone", max_length=15, blank=False)
    tem_zap = models.BooleanField("Tem Whatsapp?", default=False)
    cnae_principal = models.CharField("CNAE Principal", max_length=256, blank=True)
    cnae_secundario =  models.TextField("CNAE Principal", max_length=1024, blank=True)
    bairro = models.CharField("Bairro", max_length=64, blank=True)
    cidade = models.CharField("Cidade", max_length=64, blank=True)
    uf = models.CharField("UF", max_length=2, blank=True)

    class Meta:
        verbose_name = "Empresa"

    def __str__(self):
        return self.razao_social