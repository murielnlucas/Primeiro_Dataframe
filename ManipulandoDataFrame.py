#Retorna as primeiras linhas do dataframe 
display (Vendas.head())

#Exibe nome, tipo e valores das colunas 
print (Vendas.info())

#Retorna a estrutura do dataframe, não finaliza com () pois é um atributo e não um método
print (Vendas.shape)

#Retorna as estatísticas e médias com base nos valores das colunas 
display (Vendas.describe())

#Classifica os dados com base nas especificações fornecidas, Ascending é True para crescente e False para decrescente
display(Vendas.sort_values(["Valor Unitário"], ascending=True))

#Retornar somente 1 coluna do Dataframe, utiliza-se o print pois é somente 1 coluna, logo é uma serie e não um dataframe. Caso +1 coluna, utilize o display
print(Vendas["Produto"])

display(Vendas[["Produto", "Valor Unitário"]])

#Retorna como true ou false a condição especificada
display (Vendas[Vendas["Valor Unitário"]<50])
