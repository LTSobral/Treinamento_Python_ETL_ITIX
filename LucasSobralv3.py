import pandas as pd


def shape_head_dtypes(df):
    print("\n", df.shape, "\n\n", df.head(10), "\n\n", df.dtypes, "\n\n")


df_cad_loja_a = pd.read_excel('Datasets/CadastroLoja_A.xlsx')

df_cad_loja_b = pd.read_excel('Datasets/CadastroLoja_B.xlsx')

df_tp_cliente = pd.read_excel('Datasets/TipoCliente.xlsx')

df_vendas = pd.read_excel('Datasets/Vendas.xlsx')

# shape_head_dtypes(df_cad_loja_a)
df_cad_loja_a['CEP'] = df_cad_loja_a['CEP'].str.replace('-', '')
df_cad_loja_a['CEP'] = df_cad_loja_a['CEP'].astype(int)
# shape_head_dtypes(df_cad_loja_a)

# shape_head_dtypes(df_cad_loja_b)
df_cad_loja_b['CEP'] = df_cad_loja_b['CEP'].str.replace('-', '')
df_cad_loja_b['CEP'] = df_cad_loja_b['CEP'].astype(int)
# shape_head_dtypes(df_cad_loja_b)

# shape_head_dtypes(df_tp_cliente)

shape_head_dtypes(df_vendas)

# Exercício 03
df_vendas_loja_a = df_vendas.merge(df_cad_loja_a, left_on='ID', right_on='ID')
print("\n03 - Quais clientes da loja A fizeram compras ?\n", df_vendas_loja_a)

# Exercício 04
print("\n04 - Quais clientes da loja B fizeram compras ?\n",
      df_vendas.merge(df_cad_loja_b, left_on='ID', right_on='ID'), "\n")

# Exercício 05
print("\n05 - Quais clientes estão cadastrados nas duas lojas ?\n",
      pd.merge(df_cad_loja_a, df_cad_loja_b, left_on='ID', right_on='ID'), "\n")

# Exercício 06
print(
    "\n6 - Percebeu que as colunas ficaram com _x e da loja b _y? Quero que troque o sufixo para _a para a loja A e _b para a loja B.\n",
    pd.merge(df_cad_loja_a, df_cad_loja_b, left_on='ID', right_on='ID',
             suffixes=('_a', '_b')), "\n")

# Exercicio 07
print("\n7 - Quero ter uma base com todos os clientes de todas as lojas.\n",
      pd.concat([df_cad_loja_a, df_cad_loja_b], ignore_index=True))

# Exercicio 08
temp = pd.concat([df_cad_loja_a, df_cad_loja_b], ignore_index=True)
temp = temp.drop_duplicates(keep='first', ignore_index=True, inplace=True)
print("\n7 - Quero ter uma base com todos os clientes de todas as lojas.\n", temp)

# Exercício 09
df_merge_cad_loja_a_b = pd.merge(df_cad_loja_a, df_cad_loja_b, on=('ID', 'Idade', 'Nome',
                                                                   'CEP', 'TipoCliente'),
                                 how='outer')

# Exercício 10
df_merge_cad_loja_a_b = df_merge_cad_loja_a_b.drop_duplicates(['ID'])
print(df_merge_cad_loja_a_b)
print("\nSoma dos gastos do clientes da loja A: ", df_vendas_loja_a['Valor'].sum())

# Exercicio 11
df_temp = pd.DataFrame(df_vendas_loja_a)
del df_temp['Valor']
del df_temp['Data']
frames = [df_temp, df_cad_loja_a]
df_sem_compras_a = pd.concat(frames, ignore_index=True)
print("\n", df_sem_compras_a.drop_duplicates('ID', keep=False))

# Exercicio 12
df_vendas_loja_b = df_vendas.merge(df_cad_loja_b, left_on='ID', right_on='ID')
df_temp = pd.DataFrame(df_vendas_loja_b)
del df_temp['Valor']
del df_temp['Data']
frames = [df_temp, df_cad_loja_b]
df_sem_compras_b = pd.concat(frames, ignore_index=True)
print("\n", df_sem_compras_b.drop_duplicates('ID', keep=False))

# Exercicio 13
frame = [df_cad_loja_a, df_cad_loja_b]
df_cad_todas_lojas = pd.concat(frame, ignore_index=True)
df_cad_todas_lojas = df_cad_todas_lojas.drop_duplicates('ID')
frame = [df_vendas_loja_a, df_vendas_loja_b]
df_vendas_todas_lojas = pd.concat(frame, ignore_index=True)
df_sem_comprar_todos = pd.concat([df_vendas_todas_lojas, df_cad_todas_lojas],
                                 ignore_index=True)
df_sem_comprar_todos = df_sem_comprar_todos.drop_duplicates(keep=False)
print(df_sem_comprar_todos)

# Exercicio 14
print(df_vendas.merge(df_cad_todas_lojas, left_on='ID', right_on='ID', how='left',
                      suffixes=('', '_x')).to_string())

# Exercicio 15
df_vendas_soma = df_vendas.groupby('ID').sum('Valor')
df_vendas_soma = df_vendas_soma.sort_values('Valor', ascending=False)[0:3]
print(df_vendas_soma.merge(df_cad_todas_lojas, left_on='ID', right_on='ID'))
