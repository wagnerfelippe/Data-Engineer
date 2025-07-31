import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, inspect

# Conecta ao banco SQLite
engine = create_engine('sqlite:///covid19.db')

# Cria um inspetor e lista as tabelas
inspector = inspect(engine)
tabelas = inspector.get_table_names()

#Caminho do arquivo e a leitura do mesmo em um dataframe
caminho = 'W:/Engenharia de Dados/Specialization in Apache Airflow/Data-Engineer/Data-Engineer-1/python/cleaned_covid19.csv'
df = pd.read_csv(caminho)

# Podemos colocar uma barra quando a linha do código for muito grande
#print(df[['uf','total_resultados']]\
#                .sort_values('total_resultados', ascending=False)[:10])

#Coloco 2 columas e ordeno pelo o resultado total somente as 10 primeira linhas e faço a mesma coisa com os obitos
confirmados = df[['uf','total_resultados']].sort_values('total_resultados', ascending=False)[:10]
mortes = df[['uf','mortes']].sort_values('mortes', ascending=False)[:10]

#Colocando no gráfico as informações
confirmados[::-1].plot(
    kind='barh',
    x='uf',
    y='total_resultados',
    title='Estados com mais casos confirmados de COVID-19'
)

mortes[::-1].plot(
    kind='barh',
    x='uf',
    y='mortes',
    title='Estados com mais obitos de COVID-19',
    color='lightcoral'
)

# Envie o DataFrame para o banco de dados
df.to_sql('confirmados_obito', engine, if_exists='replace')

#Cria o select simples
resultado = 'select * from confirmados_obito limit 5'

#Coloca a query dentro da engine e atribui para o dataframe
df = pd.read_sql(resultado, engine)

#Gera a consulta das tabelas
print("Tabelas existentes")
for tabela in tabelas:
    print(f"{tabela}")

    
#print(df)
#plt.show()

