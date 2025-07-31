# Nome: Wagner
# Data: 30/07
# Descrição: Caso covid 

# ===========================================================================================
#         COMANDO DE TESTE PARA A REQUISIÇÃO DA API COVID
# ===========================================================================================
'''
try:
    response = requests.get("https://covid-api.com/api/")
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
    print(f"Status Code: {response.status_code}")
    print(f"Content Type: {response.headers['Content-Type']}")
    print(response.text[:200]) # Print first 200 characters of content
except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")
except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
            print(f"Something Else: {err}")
            
#print(f"Status Code: {response.status_code}")
#response = requests.request("GET", url, headers=headers, data=payload)
#print(response.text)            
'''

import pandas as pd
import requests

url = "https://api.covidtracking.com/v1/states/current.json"
caminho = 'W:/Engenharia de Dados/Specialization in Apache Airflow/Data-Engineer/Data-Engineer-1/python/'

response = requests.get(url)
content = response.json()

df = pd.DataFrame(content)

#Validando se existe nulo e criando variáveis para atribuição
colunas_com_nulos = df.isna().any()
colunas_sem_nulos = colunas_com_nulos[~colunas_com_nulos].index.tolist()

#Atribuindo direto em um novo dataframe
df_sem_nulos = df[colunas_sem_nulos]

#Excluindo colunas
df_sem_nulos.drop(columns=['commercialScore','negativeRegularScore','negativeScore','positiveScore','score','grade'], inplace=True)

#renomeando colunas
df_sem_nulos.columns = [
    'data', 
    'uf', 
    'positivo',
    'total_resultados_destinos',
    'total_resultados', 
    'mortes',
    'fips',
    'positivos_aumentados',
    'negativos_aumentados',
    'total',
    'total_testes_resultados',
    'posNeg',
    'mortes_aumentadas',
    'aumento_hospitalizado',
    'hash'
]

df_sem_nulos.to_csv(caminho + 'cleaned_covid19.csv', index=False)

print('Programa feito e arquivo baixo no caminho: ' , caminho)