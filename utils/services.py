import re
from django.core.validators import validate_email

class UtilsServices:
    @classmethod
    def validar_cnpj(cls, cnpj):
        # Remove caracteres não numéricos
        cnpj = re.sub(r'[^0-9]', '', cnpj)

        # Verifica se o CNPJ possui 14 dígitos após a remoção de caracteres não numéricos
        if len(cnpj) != 14:
            return False

        # Verifica se todos os dígitos são iguais (ex: 00000000000000)
        if cnpj == cnpj[0] * 14:
            return False

        # Validação do CNPJ
        multiplicadores = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = 0
        for i in range(12):
            soma += int(cnpj[i]) * multiplicadores[i]
        resto = soma % 11
        if resto < 2:
            digito_verif1 = 0
        else:
            digito_verif1 = 11 - resto

        if digito_verif1 != int(cnpj[12]):
            return False

        multiplicadores.insert(0, 6)  # Atualiza os multiplicadores para o segundo dígito verificador
        soma = 0
        for i in range(13):
            soma += int(cnpj[i]) * multiplicadores[i]
        resto = soma % 11
        if resto < 2:
            digito_verif2 = 0
        else:
            digito_verif2 = 11 - resto

        if digito_verif2 != int(cnpj[13]):
            return False

        return True
    
    @classmethod
    def validar_email(cls, email:str):
        try:
            validate_email(email)
            return True
        except :
            return False
    
    @classmethod
    def gerar_lista_uf(cls):
        return [
            {"sigla": "AC", "nome": "Acre"},
            {"sigla": "AL", "nome": "Alagoas"},
            {"sigla": "AP", "nome": "Amapá"},
            {"sigla": "AM", "nome": "Amazonas"},
            {"sigla": "BA", "nome": "Bahia"},
            {"sigla": "CE", "nome": "Ceará"},
            {"sigla": "DF", "nome": "Distrito Federal"},
            {"sigla": "ES", "nome": "Espírito Santo"},
            {"sigla": "GO", "nome": "Goiás"},
            {"sigla": "MA", "nome": "Maranhão"},
            {"sigla": "MT", "nome": "Mato Grosso"},
            {"sigla": "MS", "nome": "Mato Grosso do Sul"},
            {"sigla": "MG", "nome": "Minas Gerais"},
            {"sigla": "PA", "nome": "Pará"},
            {"sigla": "PB", "nome": "Paraíba"},
            {"sigla": "PR", "nome": "Paraná"},
            {"sigla": "PE", "nome": "Pernambuco"},
            {"sigla": "PI", "nome": "Piauí"},
            {"sigla": "RJ", "nome": "Rio de Janeiro"},
            {"sigla": "RN", "nome": "Rio Grande do Norte"},
            {"sigla": "RS", "nome": "Rio Grande do Sul"},
            {"sigla": "RO", "nome": "Rondônia"},
            {"sigla": "RR", "nome": "Roraima"},
            {"sigla": "SC", "nome": "Santa Catarina"},
            {"sigla": "SP", "nome": "São Paulo"},
            {"sigla": "SE", "nome": "Sergipe"},
            {"sigla": "TO", "nome": "Tocantins"},
        ]
