import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib

def tipocondicao(cond):
    if(cond <= 2): return 'Ruim'
    if(3 <= cond <=4): return 'Regular'
    if(cond > 4): return 'Bom'

# Exercício 01 - Leia o CSV Imóveis.csv para um dataframe
diretorio = pathlib.Path(__file__).parent.absolute()
diretorio = str(diretorio)
local = diretorio.find('PycharmProjects') + 15
dfimoveis = pd.read_csv(diretorio[:local] + '/Datasets/Imoveis.csv', encoding='utf8')

# Exercício 02 Imprima o número de colunas e o número de linhas do conjunto de dados. (Dica: shape() ).
print("Linhas, Colunas\n", np.shape(dfimoveis))

# Exercício 03 Imprima as 10 primeiras linhas do conjunto de dados (Dica: head ()
print("\n As dez primeiras linhas são:\n", dfimoveis[:10])
# OR
#  print("\n As dez primeiras linhas são:\n", dfimoveis.head(10))

# Exercício 03 Imprima os nomes das colunas do conjunto de dados (Dica: columns
print("\nAs colunas do DataFrame são: \n", dfimoveis.columns)

print("\n Os nomes das colunas foram alteradas para: \n", dfimoveis.columns)
# print("\n",dfimoveis.to_string()) UM TESTE

# Exercício 04 Imprima o datatype dos dados. (Dica dtypes)
print("\n Os tipos de dados do DataFrame são: ", dfimoveis.dtypes)

# Exercício 04 Converta a coluna “Data” para o tipo datetime
dfimoveis['data'] = pd.to_datetime(dfimoveis['data'])
print("\n O tipo de dado do da tabela data é: \n", dfimoveis['data'].dtypes)

# Exercício 05 Crie uma coluna chamada Analise e insira o ano de 2021 nela. Alterado!!
dfimoveis = dfimoveis.assign(Análise = 2021)
print("\nDataframe após a adição da coluna ANALISE: \n", dfimoveis.head(10))

# Exercício 06 Imprima na tela somente as colunas (id, data, preço, quartos, banheiros, ano de construção’)
print(dfimoveis[['data', 'preço', 'quartos', 'banheiros', 'ano de construção']])

# Exercício 07 Delete a coluna “metragem da casa.1”
del dfimoveis['metragem da casa.1']

# Exercício 08 Altere o tipo da coluna banheiros para int64.
dfimoveis['banheiros'] = dfimoveis['banheiros'].astype(str)
dfimoveis['banheiros'] = dfimoveis['banheiros'].str.replace(',', '.')
dfimoveis['banheiros'] = dfimoveis['banheiros'].astype(float).astype(int)
print(dfimoveis['banheiros'])

# Exercício 09 Imprima os imóveis com o ano de construção menor que 2000
print("\n Ano de Construção anterior a 2000:\n", dfimoveis.query('`ano de construção` < 2000'))

# Exercício 10 Altere o nome de data para DT_REFERENCIA, preço para VL_PRECO, quartos para QTD_QUARTOS, banheiros para
# QTD_BANHEIROS, ano de construção para DT_ANO_CONSTRUCAO, código postal para NU_CEP, latitude para NU_LATITUDE,
# longitude para NU_LONGITUDE, andares para QTD_ANDARES, orla para FL_ORLA e vista para FL_VISTA.

# dfimoveis.rename(columns={colunasdf[1]: 'DT_REFERENCIA'}, inplace=True)

dfimoveis.rename(columns={'data': 'DT_REFERENCIA', 'preço': 'VL_PRECO', 'quartos': 'QTD_QUARTOS', 'banheiros': 'QTD_BANHEIROS',
'ano de construção': 'DT_ANO_CONSTRUCAO', 'código postal': 'NU_CEP','latitude': 'NU_LATITUDE' ,
'longitude': 'NU_LONGITUDE', 'andares': 'QTD_ANDARES','orla': 'FL_ORLA',  'vista': 'FL_VISTA'}, inplace=True)

print("Colunas do DataFrame\n", dfimoveis.columns)

# Exercício 11 Crie uma coluna DS_TIPO_CONDICAO. Nela classifique o imóvel considerando a seguinte regra:
# - Coluna Condição < 2 então DS_TIPO_CONDICAO recebe Ruim.
# - Coluna Condição >= 3 e <= 4 então DS_TIPO_CONDICAO recebe Regular.
# - Coluna Condição > 5 então DS_TIPO_CONDICAO recebe Bom.
dfimoveis['DS_TIPO_CONDICAO'] = np.array(list(map(tipocondicao, dfimoveis['condição'].values)))

# Exercício 12 Imprima na tela o conjunto de dados ordenados pela coluna VL_PRECO de forma decrescente. Porém só quero ver as colunas Id e VL_PRECO.
dfimoveis['VL_PRECO'] = dfimoveis['VL_PRECO'].astype(str)
dfimoveis['VL_PRECO'] = dfimoveis['VL_PRECO'].str.replace(',', '.')
dfimoveis['VL_PRECO'] = pd.to_numeric(dfimoveis['VL_PRECO'])
print("ID e VL_PRECO:\n", dfimoveis.sort_values(['id','VL_PRECO'], ascending=False)['VL_PRECO'])

# Exercício 13 Imprima na tela quantos imóveis estão em condição Regular.
countregular = pd.Series(dfimoveis['DS_TIPO_CONDICAO']).str.count('Regular')
print("\nImoveis na coindição Regular são: ", countregular.sum())
# OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR QUAL E´MAIS EFICIENTE ? Ainda n sei
# print("\nImoveis na coindição Regular são: ", list(dfimoveis['DS_TIPO_CONDICAO'].values).count('Regular'))

# Exercício 14 Imprima o preço médio das casas que possuem condição Regular.
print("Preço média das casa que estão em condição REGULAR: ",dfimoveis.loc[dfimoveis['DS_TIPO_CONDICAO'] == 'Regular', ['VL_PRECO']].sum(axis=1).mean())

# Exercício 15 Imprima o preço máximo das casas com 3 quartos.
print("Preço máximo de casas com 3 quartos: ", (dfimoveis.query('QTD_QUARTOS == 3'))['VL_PRECO'].max())

# Exercício 16 Imprima a quantidade de casas em condição Boa, que possua mais de 2 quartos e mais de 2 banheiros.
print('\nQuantidade de casa em Condição BOA, que possuem mais de 2 quartos e mais de 2 banheiros: ',(dfimoveis.query('QTD_QUARTOS > 2 & QTD_BANHEIROS > 2 & condição > 4')['id'].count()))

# Exercício 17 Qual é o ID da casa com maior preço e o id da casa com menor preço.
print('\nID da casa com menor preço', dfimoveis['VL_PRECO'].idxmin(), '\nID da casa com maior preço', dfimoveis['VL_PRECO'].idxmax())

# Exercício 18 Qual a data do imóvel mais antigo no conjunto de dados ?
print('\nO ano do imovel mais antigo é: ',dfimoveis['DT_ANO_CONSTRUCAO'].min(), '\nA data de refêrencia do imovel mais antigo é: ', dfimoveis['DT_REFERENCIA'].min())
