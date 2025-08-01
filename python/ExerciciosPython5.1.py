'''
Nome: Wagner F.
Data: 31/07
Descrição: Novo código para o exercício do Covid. A API do exercício anterior não estava funcioando direto
Desta forma pegamos uma outra API para consumir os dados necessários.
'''

import pandas as pd
import requests

url_brazil = 'https://covid19-brazil-api.vercel.app/api/report/v1'
url_countries = 'https://covid19-brazil-api.vercel.app/api/report/v1/countries'
caminho = 'W:/Engenharia de Dados/Specialization in Apache Airflow/Data-Engineer/Data-Engineer-1/python/'

response = requests.get(url_brazil)
response2 = requests.get(url_countries)
#print(response)

result_br = response.json()
dados_br = result_br['data']

result_countries = response2.json()
dados_countries = result_countries['data']

df_br = pd.DataFrame(dados_br)
df_countries = pd.DataFrame(dados_countries)

del df_countries['cases']
del df_countries['recovered']

df_countries.columns = [
    'pais',
    'total_confirmados',
    'total_obitos',
    'atualização'
]

df_countries.drop(columns=['atualização'], inplace=True)

df_countries.to_csv(caminho + 'cleaned_covid19.csv', index=False)
print('Programa feito e arquivo baixo no caminho: ' , caminho)



