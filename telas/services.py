from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Empresa

class TelaServices:
    @classmethod
    def login(cls, request):
        try:
            username = request.POST.get('username', '')
            password = request.POST.get("password", '')
            print("username ", username, "password ", password)
            user = authenticate(request, username=username, password=password)
            print("user ", user)
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
            if not cnpj:
                messages.error(request, "CNPJ Campo obrigatório")
            if not ramo:
                messages.error(request, "Ramo Campo obrigatório")
            if not email:
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
    def obtem_empresas(cls, request):
        try:
            empresas = Empresa.objects.all().order_by("criado")

            context = {
                "empresas": empresas
            }
            return context
        except Exception as e:
            messages.error(request, "Erro ao listar empresas")
            return {}