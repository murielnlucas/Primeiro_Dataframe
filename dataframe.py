#Importar as bibliotecas necessárias
import pandas as pd
# as bibliotecas referentes ao Drive e ao Colab
from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Autenticação no Google Drive
auth.authenticate_user()
drive_service = build('drive', 'v3')

# Definir o ID(Código do link) do arquivo da base de dados no Google Drive
file_id = '1BxvU4htxuQPSw84PZtPsxBg35TMkVFYN'

# Definir os parâmetros de leitura do arquivo Excel
header = 0
index_col = 0
usecols = 'A:H'

# Definir o URL do arquivo a ser lido
file_url = f'https://drive.google.com/uc?id={file_id}'

# Ler o arquivo Excel usando a função read_excel do Pandas
try:
    Vendas = pd.read_excel(file_url, header=header, index_col=index_col, usecols=usecols)
    print('Base de dados importada com sucesso!')
except HttpError as error:
    print(f'Ocorreu um erro ao tentar importar a base de dados: {error}')


#Limpar as linhas duplicadas 
Vendas.drop_duplicates(subset=None, keep='first', inplace=True)

#Excluir o que está vazio 
VendasFinal = Vendas.dropna(axis=0, how="any", inplace=False)

#Iniciando a análise 

TotalVendas = Vendas['Valor Final'].sum()
TotalVendasLoja = Vendas.groupby(['ID Loja'])['Valor Final'].sum()
TotalVendasData = Vendas.groupby(['Data'])['Valor Final'].sum()
TotalVendasProduto = Vendas.groupby(['Produto'])['Valor Final'].sum()

display("Total de Vendas:" , TotalVendas)
display("Total de Vendas por loja:" , TotalVendasLoja)
display("Total de Vendas por data:" , TotalVendasData)
display("Total de Vendas por produto:" , TotalVendasProduto)

#Gera relação de vendas produto X filial
Prod_Loja = Vendas.pivot_table(Vendas, index=['ID Loja', 'Produto'], columns=None, aggfunc='sum', dropna=True, margins=False)

#Gera relação de vendas Loja X Data
Data_Loja = Vendas.pivot_table(Vendas, index=['ID Loja', 'Data'], columns=None, aggfunc='sum', dropna=True, margins=False)

