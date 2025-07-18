import pandas as pd

s = pd.Series(
    data=['Maizena','Farinha', 'Açucar', 'Ovos', 'Manteiga', 'Castanha'],  #Série de ingredientes
    index=['i1','i2','i3','i4','i5', 'i6'],
    name='Ingredientes',  #Nome
    dtype=str #String
)

s2 = pd.Series(
    data=[200, 250, 100, 2, 150, 180],
    index=['Maizena','Farinha', 'Açucar', 'Ovos', 'Manteiga', 'Castanha'],
    name='Quantidade',
    #dtype=
)



d1 = pd.DataFrame({
    'Ingredientes': ['Maizena','Farinha', 'Açucar', 'Ovos', 'Manteiga', 'Castanha'],
    'Quantidades': [200, 250, 100, 2, 150, 180]
})



#Index LOC >- index nomeado
#Index iLOC < posicional


d1.columns = ['Quantidades', 'Ingredientes']
print(d1)