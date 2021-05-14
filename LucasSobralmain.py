import pandas as pd
import numpy as np
import pathlib

def tipo_condicao(
        condicao_):
    if(condicao_ <= 2):
        return 'Ruim'
    if(3 <= condicao_ <=4):
        return 'Regular'
    if(condicao_ > 4):
        return 'Bom'
#VERIFICA a condiçao do imovel, retorna 'Ruim, Regular ou Bom'

#EXERCÍCIO 01 - Leia o CSV Imóveis.csv para um dataframe
diretorio = pathlib.Path(__file__).parent.absolute()
diretorio = str(diretorio)
local = diretorio.find('PycharmProjects') + 15
dfimoveis = pd.read_csv(diretorio[:local]
                        + '/Datasets/Imoveis.csv', encoding='utf8')


#EXERCÍCIO 02
#Imprima o número de colunas e o número de linhas do conjunto de dados.
#(Dica: shape() ).
print("Linhas, Colunas\n",
      np.shape(dfimoveis))


#EXERCÍCIO 03
#Imprima as 10 primeiras linhas do conjunto de dados (Dica: head ()
print("\n As dez primeiras linhas são:\n",
      dfimoveis[:10])
#OR
#print("\n As dez primeiras linhas são:\n", dfimoveis.head(10))


#EXERCÍCIO 03
#Imprima os nomes das colunas do conjunto de dados (Dica: columns)
print("\nAs colunas do DataFrame são: \n", dfimoveis.columns)
print("\n Os nomes das colunas foram alteradas para: \n",
      dfimoveis.columns)
#print("\n",dfimoveis.to_string()) UM TESTE


#EXERCÍCIO 04 Imprima o datatype dos dados. (Dica dtypes)
print("\n Os tipos de dados do DataFrame são: ", dfimoveis.dtypes)


#EXERCÍCIO 04 Converta a coluna “Data” para o tipo datetime
dfimoveis['data'] = pd.to_datetime(dfimoveis['data'])
print("\n O tipo de dado do da tabela data é: \n",
      dfimoveis['data'].dtypes)


#EXERCÍCIO 05 Crie uma coluna chamada Analise e insira o ano de 2021 nela.
dfimoveis = dfimoveis.assign(Análise=2021)
print("\nDataframe após a adição da coluna ANALISE: \n",
      dfimoveis.head(10))


#EXERCÍCIO 06 Imprima na tela somente as colunas
# (id, data, preço, quartos, banheiros, ano de construção’)
print(dfimoveis[['data',
                 'preço',
                 'quartos',
                 'banheiros',
                 'ano de construção']])


#EXERCÍCIO 07 Delete a coluna “metragem da casa.1”
del dfimoveis['metragem da casa.1']


#EXERCÍCIO 08 Altere o tipo da coluna banheiros para int64.
dfimoveis['banheiros'] = dfimoveis['banheiros'].astype(str)
dfimoveis['banheiros'] = dfimoveis['banheiros'].str.replace(',', '.')
dfimoveis['banheiros'] = dfimoveis['banheiros'].astype(float).astype(int)
print(dfimoveis['banheiros'])


#EXERCÍCIO 09 Imprima os imóveis com o ano de construção menor que 2000
print("\n Ano de Construção anterior a 2000:\n",
      dfimoveis.query('`ano de construção` < 2000'))


#EXERCÍCIO 10
dfimoveis.rename(columns={'data': 'DT_REFERENCIA',
                          'preço': 'VL_PRECO',
                          'quartos': 'QTD_QUARTOS',
                          'banheiros': 'QTD_BANHEIROS',
                          'ano de construção': 'DT_ANO_CONSTRUCAO',
                          'código postal': 'NU_CEP',
                          'latitude': 'NU_LATITUDE' ,
                          'longitude': 'NU_LONGITUDE',
                          'andares': 'QTD_ANDARES',
                          'orla': 'FL_ORLA',
                          'vista': 'FL_VISTA'}, inplace=True)
print("Colunas do DataFrame\n", dfimoveis.columns)


#EXERCÍCIO 11 Crie uma coluna DS_TIPO_CONDICAO.
#Nela classifique o imóvel considerando a seguinte regra:
#- Coluna Condição < 2 então DS_TIPO_CONDICAO recebe Ruim.
#- Coluna Condição >= 3 e <= 4 então DS_TIPO_CONDICAO recebe Regular.
#- Coluna Condição > 5 então DS_TIPO_CONDICAO recebe Bom.
dfimoveis['DS_TIPO_CONDICAO'] = np.array(list(map(
    tipo_condicao, dfimoveis['condição'].values)))


#EXERCÍCIO 12
#Imprima na tela o conjunto de dados ordenados pela coluna
#VL_PRECO de forma decrescente.
#Porém só quero ver as colunas Id e VL_PRECO.
dfimoveis['VL_PRECO'] = dfimoveis['VL_PRECO'].astype(str)
dfimoveis['VL_PRECO'] = dfimoveis['VL_PRECO'].str.replace(',', '.')
dfimoveis['VL_PRECO'] = pd.to_numeric(dfimoveis['VL_PRECO'])
print("ID e VL_PRECO:\n",
      dfimoveis.sort_values(['id',
                             'VL_PRECO'],
                            ascending=False)['VL_PRECO'])


#EXERCÍCIO 13 Imprima na tela quantos imóveis estão em condição Regular.
countregular = pd.Series(dfimoveis['DS_TIPO_CONDICAO']).str.count('Regular')
print("\nImoveis na coindição Regular são: ",
      countregular.sum())
#print("\nImoveis na coindição Regular são: ", list(
#                   dfimoveis['DS_TIPO_CONDICAO'].values).count('Regular'))


#EXERCÍCIO 14 Imprima o preço médio das casas que possuem condição Regular.
print("Preço média das casa que estão em condição REGULAR: ",
      dfimoveis.loc[dfimoveis['DS_TIPO_CONDICAO'] == 'Regular',
                    ['VL_PRECO']].sum(axis=1).mean())


#EXERCÍCIO 15 Imprima o preço máximo das casas com 3 quartos.
print("Preço máximo de casas com 3 quartos: ",
      (dfimoveis.query('QTD_QUARTOS == 3'))['VL_PRECO'].max())


#EXERCÍCIO 16 Imprima a quantidade de casas em condição
#Boa, que possua mais de 2 quartos e mais de 2 banheiros.
print('\nQuantidade de casa em Condição BOA,'
      ' que possuem mais de 2 quartos e mais de 2 banheiros: ',
      (dfimoveis.query('QTD_QUARTOS > 2 & QTD_BANHEIROS > 2 & condição > 4')
       ['id'].count()))


#EXERCÍCIO 17
#Qual é o ID da casa com maior preço e o id da casa com menor preço.
print('\nID da casa com menor preço',
      dfimoveis['VL_PRECO'].idxmin(),
      '\nID da casa com maior preço',
      dfimoveis['VL_PRECO'].idxmax())


#EXERCÍCIO 18 Qual a data do imóvel mais antigo no conjunto de dados ?
print('\nO ano do imovel mais antigo é: ',
      dfimoveis['DT_ANO_CONSTRUCAO'].min(),
      '\nA data de refêrencia do imovel mais antigo é: ',
      dfimoveis['DT_REFERENCIA'].min())


#EXERCÍCIO 19 De acordo com a condição do prédio,
#gostaria de saber o número de prédios pela condição,
#porém quero que seja utilizado o “groupby"
print('\nNúmeros de prédios pela condição:\n',
      dfimoveis.groupby(['DS_TIPO_CONDICAO'])['id'].count())


#EXERCÍCIO 20 Qual é o preço médio dos imóveis por ano de construção?
print('\nPreço médio por ano de construçãõ: \n',
      dfimoveis.groupby(['DT_ANO_CONSTRUCAO'])['VL_PRECO'].mean('VL_PRECO'))


#EXERCÍCIO 21 Qual é o menor número de quartos por
#ano de construção de imóveis
print('\nMenor número de quartos por ano de construção: \n',
      dfimoveis.groupby(['DT_ANO_CONSTRUCAO'])
      ['QTD_QUARTOS'].min('QTD_QUARTOS'))


#EXERCÍCIO 22 Qual é a soma do preço dos imóveis por número de
# quartos e banheiros? (Obs: cuidado com a ordem)
print('\nSoma dos preços dos imoveis por quartos e banheiros: \n',
      dfimoveis.groupby(['QTD_QUARTOS', 'QTD_BANHEIROS'])
      ['VL_PRECO'].sum('VL_PREÇO'))


#EXERCÍCIO 23 Qual é a mediana do preço dos imóveis por ano ?
print('\nMediana do preço dos imoveis por ano: \n',
      dfimoveis.groupby(['DT_ANO_CONSTRUCAO'])['VL_PRECO'].median())


#EXERCÍCIO 24 Classifique os imóveis de acordo com o seu preço
#Preço  <321950    = 0
#Preço >= 321950 e <= 450000   = 1Preço > 450000
#<= 645000   = 2
#Preço > 645000    = 3
#dfimoveis.loc[dfimoveis['VL_PRECO'] < 321950, 'Classificação'] = 0
#dfimoveis.loc[(dfimoveis['VL_PRECO'] >= 321950) &
# (dfimoveis['VL_PRECO'] <= 450000), 'Classificação'] = 1
#dfimoveis.loc[(dfimoveis['VL_PRECO'] > 450000) &
# (dfimoveis['VL_PRECO'] <= 645000), 'Classificação'] = 2
#dfimoveis.loc[dfimoveis['VL_PRECO'] > 645000, 'Classificação'] = 3
# print('\nClassificação utilizando loc: \n', dfimoveis['Classificação'])



#EXERCÍCIO 25 Repita o exercício 24,
#porém agora faça a classificaçãousando expressão lambda
dfimoveis['Classificação'] = list(map(lambda x: 0 if x < 321950 else
            3 if x > 645000 else
            1 if (x >= 321950) & (x <= 450000) else
            2 if (x > 450000) & (x <= 645000) else
            np.nan, dfimoveis['VL_PRECO'])) #Classifica imoveis
print('\nClassificação utilizando lambda: \n', dfimoveis['Classificação'])


#EXERCÍCIO 26
df = pd.DataFrame(dfimoveis.groupby('NU_CEP')[['id',
                                               'VL_PRECO',
                                               'NU_CEP']].mean('VL_PRECO'))
df.to_csv('arquivo.csv', index=False, header=True)
print('\nArquivo Exportado como arquivo.csv\n',df)