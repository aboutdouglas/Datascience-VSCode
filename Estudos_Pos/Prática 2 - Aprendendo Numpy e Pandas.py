import matplotlib.pyplot as plt
import pandas as pd

gamedata = pd.read_csv('./at2-vgsales.csv')
print(gamedata.head(10))

gamedata.columns = ['Ranking', 'Nome', 'Plataforma', 'Ano','Gênero', 'Produtora',
                    'Vendas América do Norte', 'Vendas EUA', 'Vendas Japão', 'Outras vendas', 'Vendas Global']
print(gamedata.shape)
print(gamedata.head(10))

print(gamedata.describe())

# Selecionando uma coluna:
print(gamedata['Nome'])

# Selecionando varias colunas:
print(gamedata[['Nome', 'Ano']])

# pegar da linha 2 até a linha 10:
print(gamedata[['Ranking', 'Nome']][2:10])

# pegar da linha 0 até a linha 15:
print(gamedata[['Ranking', 'Nome']][:15])

# pegar as 8 ultimas linhas:
print(gamedata[['Ranking', 'Nome']][-8:])

# retornando da linha 10 até a linha 20:
print(gamedata[['Ranking', 'Nome']][10:20])

# retornando as 20 últimas linhas dos campos Genero e Ranking:
print(gamedata[['Gênero', 'Ranking']][-20:])

# retornando as 10 primeiras linhas dos campos Vendas USA e Vendas Japão:
print(gamedata[['Vendas EUA', 'Vendas Japão']][:10])

# verificar quais linhas que possuem a coluna Ano nulo:
nullrows = gamedata['Ano'].isnull()
print(gamedata[nullrows].head(5))

# sumarizar dados:
print(gamedata['Plataforma'].value_counts())


df = pd.DataFrame(gamedata, columns=['Nome', 'Vendas EUA'])

# menor valor de um DataFrame:
print(df.min())

# maior valor de um DataFrame:
print(df.max())

# index do menor valor:
#print(df.idxmin())

# index do maior valor:
#print(df.idxmax())

# média de valores:
print(df.mean())

# mediana de valores:
print(df.median())

# soma:
print(df['Vendas EUA'].sum())

# conte a frequencia de cada genero na coluna Gênero:
print(gamedata['Gênero'].value_counts())

# selecione todos os registros em que o campo Ano NÃO é nulo:
notnullrows = gamedata['Ano'].notnull()
print(gamedata[notnullrows].head(5))

# exiba a média das "Vendas no Japão" e "Vendas nos EUA":
print("Média Vendas EUA: ", gamedata['Vendas EUA'].mean())
print("Média Vendas Japão: ", gamedata['Vendas Japão'].mean())

# exiba o valor mínimo de venda na coluna "Outras Vendas":
print("Mínimo Outras vendas: ", gamedata['Outras vendas'].min())

# exiba a soma total das "Outras vendas" e "Vendas Global"
print("Soma de Outras vendas: ", gamedata['Outras vendas'].sum())
print("Soma Vendas Global: ", gamedata['Vendas Global'].sum())

# ordenação de colunas:
print(gamedata.sort_values(['Nome',"Ano"], ascending=True))

# ordene os dados pelo Nome e pela Produtora de forma ascendente:
print(gamedata.sort_values(['Nome', 'Produtora'], ascending=True))

# ordene os dados pelo Ranking e pelo Ano de forma decrescente:
print(gamedata.sort_values(['Ranking', 'Ano'], ascending=False))

# exiba os dados da coluna Plataforma ordenados de forma descrescente pelas "Vendas Globais":
dataf = pd.DataFrame(gamedata, columns=['Plataforma', 'Vendas Global'])
print(dataf.sort_values(['Vendas Global'], ascending=False))

# cruzamento de dados:
cruzamentoDados = pd.crosstab(gamedata['Plataforma'], gamedata['Gênero'])
print(cruzamentoDados.head(10))

# cruzamento dados selecionados:
cruzamentoDados['Total'] = cruzamentoDados.sum(axis=1)
top_platforms = cruzamentoDados[cruzamentoDados['Total'] > 2000]
print(top_platforms.head(10))

# ordene a tabela pela coluna "Total" de forma decrescente:
print(cruzamentoDados.sort_values(['Total'], ascending=False))

# selecione todas as plataformas que tiveram vendas abaixo de 100 unidades do genero Adventure:
df_adv = pd.DataFrame(cruzamentoDados, columns=['Adventure', 'Total'])
top_adventures = df_adv[df_adv['Adventure'] > 100]
print(top_adventures)

# pegue o resultado da atividade anterior e ordene de forma crescente
print(top_adventures.sort_values(['Adventure'], ascending=True))

plt.bar(dataf['Plataforma'], dataf['Vendas Global'])
plt.title('VENDAS DE CONSOLE PELO MUNDO')
plt.xlabel('PLATAFORMA')
plt.ylabel('VENDAS')
plt.show()