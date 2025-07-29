'''
Nome: Wagner F.
Data: 28/07
Descrição: Este projeto tem como objetivo simular uma situação real de análise de dados,
onde você atuará como analista ou engenheiro de dados em uma empresa
responsável por realizar uma prova de redação em nível nacional. O projeto
abrange diversas etapas, desde a criação de um conjunto de dados (dataset) até
a geração de visualizações e relatórios
'''

# Valores que testamos antes de colocar dentro do código

#print((np.random.uniform(0, 1000.1, amostra)  > 1000).any()) # Validação de valores maiores que 1000 e se existe algum valor TRUE
#print((np.random.choice(sexo, amostra) == 'M').sum() ) # Validar os valores masculinos e depois somar quantos valores existem do sexo M.



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Semente usada para manter os mesmos números aleatórios
seed = 0
np.random.seed(seed) 

# Lista de datas entre períodos
datas = pd.date_range('2000-01-01', '2000-01-31')

# Criando uma lista de sexo
sexo = ['M', 'F']

# Criando uma lista de estados
estado = [ 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 
    'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 
    'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

# Quantidade de valores de amostra(Tamanho)
amostra = 1000

df = pd.DataFrame(
    {
        'idade' : np.random.randint(0, 101, amostra), # numeros aleatorios de 0 a 100 com base no tamanho da amostra (100)
        'data'  : np.random.choice(datas, amostra), # Datas aleatórias de 2000-01-01 até 2000-01-31 do tamanho da amostra
        'nota'  : np.random.uniform(0, 1000.1, amostra), # Notas aleatórias até 1000 de acordo com o tamanho da amostra
        'sexo'  : np.random.choice(sexo, amostra), # Sexo aleatório com base no tamanho da amostra
        'estado': np.random.choice(estado, amostra) # Estados aleatorios de acordo com a lista e o tamanho da amostra
    }
)


#Transformar 20% das notas em valores nulos
ausentes = df.sample(frac=.2, random_state=seed).index
valores_nulos = df.loc[ausentes, 'nota'] = np.nan

#Colocar os valores nulos que estão na nota em zero(0).

#df.fillna(0)
#df.loc[ausentes, 'nota'] = 0
valores_zeros = df.loc[df['nota'].isna(),'nota'] = 0

# remover idades de menor de 18 e maior que 80
# Existem 2 jeitos de fazer

# Jeito 1
'''mask_lt18 = df['idade'] < 18
mask_gt80 = df['idade'] > 80
mask_wrongAge = mask_lt18 | mask_gt80
df.drop(df[mask_wrongAge].index)'''

# Jeito 2
mask_gt18 = df['idade'] >= 18
mask_lt80 = df['idade'] <= 80
mask_ValideAge = mask_gt18 & mask_lt80
df = df[mask_ValideAge]


# Criando um novo campo dentro do dataframe chamado aprovado que contem somente os alunos que atingiram as notas acima de 600
# teste = df['nota'].apply(aprovado).value_counts() #Contando a quantidade de valores reprovados e aprovados 

#Criando a função de aprova e reprovado
aprovado = lambda x: 'Aprovado' if x >= 600 else 'Reprovado'

#Aqui já crio a coluna no dataframe utilizando a função acima, através do campo da nota.
df['aprovado'] = df['nota'].apply(aprovado)


df['dia_semana'] = df['data'].dt.weekday #Monday=0, Sunday=6


print(df.tail(30))



