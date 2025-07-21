import pandas as pd
import numpy as np

s = pd.Series(
    data=['Maizena','Farinha', 'Açucar', 'Ovos', 'Manteiga', 'Castanha'],  #Série de ingredientes
    index=['i1','i2','i3','i4','i5', 'i6'],
    name='Ingredientes',  #Nome
    dtype=str #String
)

s2 = pd.Series(
    data=[200, 250, 100, 2, 150, 180],
    index=['Maizena','Farinha', 'Açucar', 'Ovos', 'Manteiga', 'Castanha'],
    name='Quantidade'
    #dtype=
)



df = pd.DataFrame({
    'Ingredientes': ['Maizena','Farinha', 'Açucar', 'Ovos', 'Manteiga', 'Castanha'],
    'Quantidades': [200, 250, 100, 2, 150, 180]
})



#Index LOC >- index nomeado
#Index iLOC < posicional
df.columns = ['Ingredientes','Quantidades']
#d1 = df['Quantidades']
#print(d1)


#df.iloc[3, 1] = 3

# print(type(df)) #Olhamos o tipo do dataframe
# print(df) #realizamos o print do datafraa

#print(df.iloc[3, 'Quantidades'])
# df.iloc[3, 1] = 3 # Eu tenho que usar neste formato e não direto no print. Ele não reconhece o comando. Transformo a minha quantidade da Linha 3(indice numeral), Coluna 1 (Quantidades) em valor 3.
#print(df)

#print(df.dtypes) #Lendo o tipo de dados do dataframe


####################################################### NOVA AULA ###################################################################
# read_* -> Leitura
# to_* -> escrita


df = pd.read_csv("W:/Engenharia de Dados/Backup/Electric_Vehicle_Population_Data.csv") #Lendo o arquivo normalmente em csv
#print(df.head(10)) #trazendo somente as 10 primeiras linhas (de 0 a 9)
#print(df.tail(10)) #trazendo somente as 10 últimas linhas
#print(df.T) #mostrando os dados transposto. Neste caso as linhas se tornam em coluna.
#print(df.info()) #comando para mostrar informações necessárias das colunas
#print(df.sample(100)) #comando para mostrar informações necessárias das colunas

#df.loc[50:150, 'Postal Code'] = np.nan
#print(df) #comando para mostrar informações necessárias das colunas

#print(df.info())
#print(df.isnull().sum()) #olhando quantos valores nullos tem na planilha em cada coluna
#print(df.isnull().any()) #olhando se existem valores nulos como true ou false
#print(df.duplicated().any()) #olhando se existem valores duplicados na planilha
#df.drop_duplicated() #Elimita as duplicadas
#print(df.sort_values('Postal Code'), ascending=False) #ordenando valores pelo postal code de forma decrescente
#print(df['Postal Code'].nunique()) #Qtde de valores únicos
#print(df['Postal Code'].unique()) #Amostra dos valores únicos

#print(df['Postal Code'].value_counts()) #contar quantos valores tem a coluna postal Code
#print(df.groupby('Postal Code')['Model Year'].max()) #Agrupando valores do Postal Code por Ano

#df2 = df.groupby('Postal Code')['Model Year'].agg(['min','mean','max']) #Agrupando valores do Postal Code minimo, médio, e máximo
#print(df2.melt()) #Dados transposto para linha, variavel de agg e o ano

#mask_grt2022 = df[df['Postal Code'] > 2022]
#print(mask_grt2022) #Traz os valores das colunas referente a quem tem o ano maior que 2022. 
#print(mask_grt2022[['Postal Code', 'County', 'City']]) #Puxando somente 3 colunas de onde o meu postal code é maior que 2022
#print(mask_grt2022.describe()) #descrição dos valores, média, min, máxima, counts, etc.

#def age_days(idade):
#    return idade * 365
#print(df['Postal Code'].apply(age_days)) # utilizando função em uma coluna.

#print(df[['Legislative District','Base MSRP']])

#print( pd.crosstab(df['Base MSRP'], df['Legislative District']) ) #Base MSRP por Legislative. COmo se fosse uma tabela dinamica. Tamém podemos usar o pivotable

#df.rename(index{0: 1000}, column={'Series': 'Z'}) #Renomeando valores
