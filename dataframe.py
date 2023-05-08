#Importar as bibliotecas necessárias
#Precisa importar as bibliotecas da nuvem, nesse caso do drive
import pandas as pd
from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Autenticar-se no Google Drive
auth.authenticate_user()
drive_service = build('drive', 'v3')

# Definir o ID do arquivo da base de dados no Google Drive
#Esse ID você pega o código direto do link da planilha
file_id = '1BxvU4htxuQPSw84PZtPsxBg35TMkVFYN'

# Definir os parâmetros de leitura do arquivo Excel
header = 0
index_col = 0
usecols = 'A:G'

# Definir o URL do arquivo a ser lido
file_url = f'https://drive.google.com/uc?id={file_id}'

# Ler o arquivo Excel usando a função read_excel do Pandas
try:
    Vendas = pd.read_excel(file_url, header=header, index_col=index_col, usecols=usecols)
    print('Base de dados importada com sucesso!')
except HttpError as error:
    print(f'Ocorreu um erro ao tentar importar a base de dados: {error}')

print (Vendas.shape)
