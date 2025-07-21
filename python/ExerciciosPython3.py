'''
Name: Wagner F.
Date: 20/07/25
Description: Using a example of the data frame to pratice with charts month and temperature
'''

#Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#criação do data frame
df = pd.DataFrame({
    'month': ['jan','fev','mar','abr','mai','jun','jul','ago'],
    'temperature': [29, 26, 25, 20, 18, 17, 16, 18]
 }
)

ax = df.plot(
    kind = 'bar', #estilo do gráfico
    figsize = (6,4), #tamanho do gráfico
    x = 'month', #eixo x
    y = 'temperature', #eixo y
    color = 'red', #cor da gráfico
    yticks = [0,10,20,30,40], #Intervalo do eixo y 
    ylim = [0, 40], #limit until 40
    xlabel = 'month', #lable x
    ylabel = 'ºC', #lable y
    title = 'Temperature in 2023', #title
    grid = False, #with grid
    rot = 45, #rotation
    width = 0.8 #large bar
)

# Adicionar os valores no topo de cada barra
for bar in ax.patches:
    ax.annotate(
        f'{bar.get_height()}', # Texto (valor da barra)
        (bar.get_x() + bar.get_width() / 2, bar.get_height()),  # Posição (x, y)
        ha = 'center',
        va = 'bottom',
        fontsize = 10,
        color = 'black'
    )
plt.tight_layout()
plt.show()
