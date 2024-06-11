import csv
import pandas as pd
from django.contrib import messages
from telas.models import Empresa
import chardet


class MineracoeServices:
    @classmethod
    def subir_arquivo(cls, request):
        try:
            uploaded_file = request.FILES.get('arquivo')

            if uploaded_file:
                if uploaded_file.name.endswith('.csv'):
                    return cls.handle_csv_file(uploaded_file)
                elif uploaded_file.name.endswith('.xlsx') or uploaded_file.name.endswith('.ods'):
                    return cls.handle_excel_file(uploaded_file)
                else:
                    messages.error(request, 'Tipo de arquivo não suportado.')
                    return True
        except Exception as e:
            print("ERRO ao subir arquivo ", e)
            return False
    
    @classmethod
    def handle_csv_file(cls, file):
        # Detectar a codificação do arquivo
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

        # Re-abrir o arquivo com a codificação detectada
        file.seek(0)
        decoded_data = raw_data.decode(encoding).splitlines()
        reader = csv.DictReader(decoded_data)
        for row in reader:
            print(row)
            empresa = Empresa(
                razao_social=row.get('razao_social', '').strip(),
                cnpj=row.get('cnpj', '').strip(),
                ramo=row.get('atividade_principal', '').strip(),
                email=row.get('contato_email_1', '').strip(),
                fone=row.get('contato_telefonico_1', '').strip(),
                tem_zap=False,  # Isso pode ser ajustado conforme necessário
                cnae_principal=row.get('atividade_principal', '').strip(),
                bairro=row.get('bairro', '').strip(),
                cidade=row.get('municipio', '').strip(),
                uf=row.get('uf', '').strip(),
            )
            empresa.save()

    @classmethod
    def handle_excel_file(cls, file):
        df = pd.read_excel(file, dtype=str)
        for _, row in df.iterrows():
            print(row)
            empresa = Empresa(
                razao_social=row.get('razao_social', '').strip(),
                cnpj=row.get('cnpj', '').strip(),
                ramo=row.get('atividade_principal', '').strip(),
                email=row.get('contato_email_1', '').strip(),
                fone=row.get('contato_telefonico_1', '').strip(),
                tem_zap=False,  # Isso pode ser ajustado conforme necessário
                cnae_principal=row.get('atividade_principal', '').strip(),
                bairro=row.get('bairro', '').strip(),
                cidade=row.get('municipio', '').strip(),
                uf=row.get('uf', '').strip(),
            )
            empresa.save()


 