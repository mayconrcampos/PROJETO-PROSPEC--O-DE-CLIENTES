from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Empresa
from utils.services import UtilsServices


class TelaServices:
    @classmethod
    def login(cls, request):
        try:
            username = request.POST.get('username', '')
            password = request.POST.get("password", '')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Usuário logado com sucesso")
                return True
            messages.error(request, "Credenciais inválidas")
            return False
        except Exception as e:
            messages.error(request, "Erro ao tentar fazer login")
            return False
    
    @classmethod
    def logout(cls, request):
        try:
            logout(request=request)
            return True
        except Exception as e:
            return False
    
    @classmethod
    def cadastra_empresa(cls, request):
        try:
            razao_social = request.POST.get("razao_social", '')
            cnpj = request.POST.get("cnpj", '')
            ramo = request.POST.get("ramo", '')
            email = request.POST.get("email", '')
            telefone = request.POST.get("telefone", '')
            tem_Zap = request.POST.get("tem_zap", '')
            cnae_principal = request.POST.get("cnae_principal", '')
            cnae_secundario = request.POST.get("cnae_secundario", '')
            bairro = request.POST.get("bairro", '')
            cidade = request.POST.get("cidade", '')
            uf = request.POST.get("uf", '')

            if not razao_social:
                messages.error(request, "Razão Social Campo obrigatório")
            if not UtilsServices.validar_cnpj(cnpj=cnpj):
                messages.error(request, "CNPJ Campo obrigatório")
            if not ramo:
                messages.error(request, "Ramo Campo obrigatório")
            if email:
                if not UtilsServices.validar_email(email=email):
                    messages.error(request, "Email Campo obrigatório")
            if not telefone:
                messages.error(request, "Telefone Campo obrigatório")
            
            tem_Zap = True if tem_Zap == "1" else False

            empresa = Empresa(
                razao_social=razao_social,
                cnpj=cnpj,
                ramo=ramo,
                email=email,
                fone=telefone,
                tem_zap=tem_Zap,
                cnae_principal=cnae_principal,
                cnae_secundario=cnae_secundario,
                bairro=bairro,
                cidade=cidade,
                uf=uf
            )
            empresa.save()

            messages.success(request, "Empresa cadastrada com sucesso")
            return True
        except Exception as e:
            print("erro ", e)
            messages.error(request, "Erro ao cadastrar empresa")
            return False
    
    @classmethod
    def atualiza_empresa(cls, request):
        try:
            razao_social = request.POST.get("razao_social", '')
            cnpj = request.POST.get("cnpj", '')
            ramo = request.POST.get("ramo", '')
            email = request.POST.get("email", None)
            telefone = request.POST.get("telefone", '')
            tem_Zap = request.POST.get("tem_zap", '')
            cnae_principal = request.POST.get("cnae_principal", '')
            cnae_secundario = request.POST.get("cnae_secundario", '')
            bairro = request.POST.get("bairro", '')
            cidade = request.POST.get("cidade", '')
            uf = request.POST.get("uf", '')

            empresa_id = request.POST.get("empresa_id", '')

            empresa = Empresa.objects.filter(id=empresa_id)

            if empresa:
                empresa = empresa.first()

                empresa.razao_social = razao_social
                empresa.cnpj = cnpj
                empresa.ramo = ramo
                empresa.email = email
                empresa.fone = telefone
                empresa.tem_zap = tem_Zap
                empresa.cnae_principal = cnae_principal
                empresa.cnae_secundario = cnae_secundario
                empresa.bairro = bairro
                empresa.cidade = cidade
                empresa.uf = uf

                empresa.save()

                messages.success(request, "Dados da empresa atualizados com sucesso")
                return True
            messages.error(request, "Empresa não encontrada")
            return False
        except Exception as e:
            print("erro atualiza empresa ", e)
            return False
    
    @classmethod
    def excluir_empresa(cls, request):
        try:
            empresa_id = request.POST.get("empresa_id", '')

            empresa = Empresa.objects.filter(id=empresa_id).first()

            empresa.delete()

            messages.success(request, "Empresa excluida com sucesso")
            return True
        except Exception as e:
            print("Erron ao excluir empresa ", e)
            return False
    
    @classmethod
    def obtem_empresas(cls, request):
        try:
            empresas = Empresa.objects.all().order_by("-criado")
            ufs = UtilsServices.gerar_lista_uf()

            context = {
                "empresas": empresas,
                "ufs": ufs
            }
            return context
        except Exception as e:
            messages.error(request, "Erro ao listar empresas")
            return {}