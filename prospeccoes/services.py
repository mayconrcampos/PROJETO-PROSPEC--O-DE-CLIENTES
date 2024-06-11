from telas.models import Empresa
from .models import Prospeccao
from django.db.models import Subquery, OuterRef, Q, BooleanField, TextField
from django.contrib import messages
from django.core.paginator import Paginator



class ProspeccoeServices:
    @classmethod
    def obter_prospeccoes(cls, request, page=None):
        try:
            procurar = request.POST.get("procurar", '')
            print("procurar ", procurar)

            # Subquery para buscar informações de prospecção
            subquery = Prospeccao.objects.filter(empresa__id=OuterRef('id'))
            filtro = Q(razao_social__icontains=procurar) | Q(ramo__icontains=procurar) | Q(fone__icontains=procurar)

            # Anotação com subquery
            if not procurar:
                print("procurando")
                empresas = Empresa.objects.annotate(
                    msg_enviada=Subquery(subquery.values('msg_enviada'), output_field=BooleanField()),
                    cliente_respondeu=Subquery(subquery.values('cliente_respondeu'), output_field=BooleanField()),
                    indicado=Subquery(subquery.values('indicado'), output_field=BooleanField()),
                    comentarios=Subquery(subquery.values('comentarios'), output_field=TextField())
                )
                print("count ", empresas.count())
            else:
                print("nao procurando")
                empresas = Empresa.objects.filter(filtro).annotate(
                    msg_enviada=Subquery(subquery.values('msg_enviada'), output_field=BooleanField()),
                    cliente_respondeu=Subquery(subquery.values('cliente_respondeu'), output_field=BooleanField()),
                    indicado=Subquery(subquery.values('indicado'), output_field=BooleanField()),
                    comentarios=Subquery(subquery.values('comentarios'), output_field=TextField())
                )
                print("count ", empresas.count())

            empresas = empresas.order_by('-modificado')
            paginator = Paginator(empresas, 50)
            
            page = request.GET.get('page', page)
            
            pagina_atual = paginator.get_page(page)

            context = {
                'empresas': pagina_atual,
                'paginator': paginator
            }

            return context
        except Exception as e:
            print("Erro ao obter prospecções ", e)
            return {}
    
    @classmethod
    def registrar_prospeccao(cls, request):
        try:
            page = request.POST.get('page', 1)
            empresa_id = request.POST.get("empresa_id", '')
            msg_enviada = request.POST.get('msg_enviada', '')
            cliente_respondeu = request.POST.get('cliente_respondeu', '')
            indicado = request.POST.get('indicado', '')
            comentario = request.POST.get('comentario', '')

            msg_enviada = True if msg_enviada else False
            cliente_respondeu = True if cliente_respondeu else False
            indicado = True if indicado else False

            empresa = Empresa.objects.filter(id=empresa_id).first()

            if not empresa:
                messages.error(request, "Empresa não encontrada")
                return False

            prospeccao, created = Prospeccao.objects.get_or_create(
                empresa=empresa,
                defaults={
                    'msg_enviada': msg_enviada,
                    'cliente_respondeu': cliente_respondeu,
                    'indicado': indicado,
                    'comentarios': comentario
                }
            )

            if not created:
                # Atualizar prospeccao, sem reverter os campos True para False
                if prospeccao.msg_enviada:
                    msg_enviada = True
                if prospeccao.cliente_respondeu:
                    cliente_respondeu = True
                if prospeccao.indicado:
                    indicado = True

                prospeccao.msg_enviada = msg_enviada
                prospeccao.cliente_respondeu = cliente_respondeu
                prospeccao.indicado = indicado
                prospeccao.comentarios = comentario

                prospeccao.save()

                messages.success(request, "Prospecção atualizada com sucesso")
            else:
                messages.success(request, "Prospecção criada com sucesso")

            return page
                
        except Exception as e:
            print("Erro ao registrar prospecção ", e)
            return page