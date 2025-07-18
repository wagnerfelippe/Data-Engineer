'---------------------------'
#numero = input("Digite um numero: ")
#print(f"O numero digitado foi: {numero}")


'---------------------------'
#num1 = int(input("Digite o 1º numero: "))
#num2 = int(input("Digite o 2º numero "))
#print(num1 + num2)


'---------------------------'
#num1 = int(input("Digite o 1º numero: "))
#num2 = int(input("Digite o 2º numero "))
#if num1 > num2:
#    print(f"O maior número é o: {num1}")
#else:
#    print(f"O maior número é o: {num2}")



'---------------------------'
#letra = input("Digite uma letra: ")
#if letra == 'a' or letra == "A":
#    print("A letra é uma Vogal")
#elif letra == 'e' or letra == "E":
#    print("A letra é uma Vogal")
#elif letra == 'i' or letra == "I":
#    print("A letra é uma Vogal")
#elif letra == 'o' or letra == "O":
#    print("A letra é uma Vogal")
#elif letra == 'u' or letra == "U":
#    print("A letra é uma Vogal")
#else:
#    print("A letra é consoante")




'---------------------------'


#nota = int(input("Nota entre 0 e 10: "))
#if nota >= 0 and nota <= 10:
#    print("Valido")
#else:
#    print("Invalido")


#nota = int(input("Nota entre 0 e 10:\n"))
#while not(nota >=0 and nota <= 10):
#    print("Valor Inválido")
#    nota = int(input("Nota entre 0 e 10"))
#else:
#    print("Valor Válido")
#


#for numero in range(1,21):
#    print(numero)

#parada = 21
#passo = 1
#while passo < parada:
#    print(passo)
#    passo += 1

#'''
#
#numero = int(input('Nota entre 0 e 10: '))
#while not(numero >= 0 and numero <= 10):
#    print('Numero Válido')
#    numero = int(input('Nota entre 0 e 10'))
#else:
#    for passo in range(0, 11):
#        print(f'{numero} X {passo} = {numero * passo}')
#        #print(f'{numero X passo}' = numero * passo ) **/
#'''



#Dicionario 

#dicionario = {
#    'Teste 1': 10,
#    'Teste 2': 20,
#    'Teste 3': 30
#}
#print(dicionario.setdefault("Teste 1","valido"))

#help(list)


#def soma(parametro1, parametro2):
    #return parametro1 + parametro2

#a = int(input("Valor 1: "))
#b = int(input("VAlor 2: "))

#print(soma(a,b))




#def main():
#import time - função para usar o time sleep
# print('-' * 30) - Aqui eu multiplico o meu caractere em 30x 
# time.sleep(3) - função para executar por um determinado tempo

# Função para fazer um menu interativo com funções básicas.
'''import time
def main():
    while True:
        print('1 - funcao 1')
        print('2 - funcao 2')
        print('3 - Sair')

        resposta = int(input("Qual funcao?\n"))

        if resposta == 1:
            print("Escolheu a função 1")
            time.sleep(3) 

        elif resposta == 2:
            print("Escolheu a função 2")
            time.sleep(3) 
        
        elif resposta == 3:
            print("Saindo do programa!")
            time.sleep(3) 
            break
            
        else:
            print("Opcao Inválida")
            main()
main()'''


#Precisei criar uma pasta __init__.py para configuração. Ela pode ser vazia. É somente para o python entender que tem esse arquivo para puxar.
# Depois criar o arquivo com as funções que eu preciso utilizar.
# Após isso, eu consigo fazer o import da pasta e as suas funções


#import Geometria.areas as ars
#print(ars.area_triangulo(2,2))


#import os
#print(os.name)

#import os as o
#print(help(o))

########### NUMPY ############

#import numpy as np
#s_lista = [[10,6,4,8],[5,6,5,6]]
#print(np.array(s_lista))
#s_vetor = np.array(s_lista)

## [semestre, prova] = UTilizando o vetor(array).
## um exemplo é usar a s_lista[0][-1] porém com o vetor é de forma mais objetiva e clara.
#print(s_vetor[0,-1])
#s_vetor.ndim - Descorbri quantas dimensões tem dentro do vetor
#

#print(s_vetor % 2) - descobrir par dentro do array / Máscara

# Operação boleanas dentro do vetor
# not -> ~
# and -> &
# or -> | 
# xor -> ^
#
#e_par = s_vetor % 2 == 0
#
# print(s_vetor[~ e_par])


#a_lista = [
#    s_lista,
#    s_lista
#]
#print(a_lista)

#a_vetor = np.array(a_lista)
#print(a_vetor)

# as camadas do vetor é [ano, semestre, prova]
#print(a_vetor[1, 0, -1])



#a_vetor[1, :, :] += 1 # Estou pegando o segundo ano [0 e 1], todos os sementes e todas as provas.
#print(a_vetor[0, 1, 0])

#print(np.random.randint(0, 6, 10)) #Aqui vai ser um intervalo de 0 a 6 com 10 números

#arr = np.array([5, 2, 8, 1, 3])
#print(np.sort(arr)) #Ordenação do array

#arr2 = np.array([[3,1,2], [4,6,5]])
#print(np.sort(arr2, axis=1)) #Ordenação do multiarray


#O NumPy permite buscar e filtrar elementos em arrays com base em condições específicas
#arr3 = np.array([1,2,3,4,5])
#mask = arr3 > 2
#print(np.where(arr3 > 3))
#print(arr3[mask])





# =======================================================================================================
#                 ===================  COMANDOS MATPLOTLIB ============================
# =======================================================================================================


# =======================================================================================================
#                 ===================  GRÁFICO DE BARRAS ============================
# =======================================================================================================

'''
import matplotlib.pyplot as plt
import numpy as np

mes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago']
temperatura = [29, 26, 25, 20, 18, 17, 16, 18, ]

#plt.plot(mes, temperatura)

plt.figure(figsize=(12,6))
#Aqui precisei colocar o plt.bar dentro de uma variável barras. 
#Como se fosse um container para conseguir colocar os rótulos de dados.
barras = plt.bar(mes, temperatura, color='green')
plt.yticks([10,20,30])
plt.ylim([0, 40])
plt.bar_label(barras, fmt='%g')
plt.xlabel("meses")  
plt.title("Temperatura em Cº por meses")


plt.show()'''


# =======================================================================================================
#                 ===================  GRÁFICO DE PIZZA ============================
# =======================================================================================================

'''
import matplotlib.pyplot as plt
import numpy as np

valores = [15,30,45,10] #Valores do gráfico setado na mão
rotulos = ['Frogs', 'Hogs', 'Dogs', 'Logs'] #Rótulo/Legenda do gráfico
destaque = [0, .05, 0, 0] # Aqui é qual fatia terá destaque
plt.figure(figsize=(10,10)) # Tamanho da figura

#Configurações do gráfico
plt.pie(valores, 
        explode=destaque, #pegando a função de selecionar a fatia de destaque
        labels=rotulos,   #Colocando os rótulos
        autopct='%.1f%%', #Colocando os valores me porcentagem
        shadow=True,      #Colocando as sombras
        startangle=90     #Colocanco o começo do gráfico em 90º
)
#Comando para mostrar o gráfico
plt.show()'''



# =======================================================================================================
#                 ===================  GRÁFICO DE DISPERSÃO ============================
# =======================================================================================================

'''
import matplotlib.pyplot as plt
import numpy as np

x = [.8, 2.4, 3.3, 4, 4.4, 5]
y = [63, 34, 22, 48, 18, 5]

tamanho = np.array([10, 6, 3, 8, 2, 10]) * 20  #Tamanho da bola
cores = ['red', 'green', 'yellow', 'yellow', 'green', 'red'] #Cor da bola na orgem que são os números
plt.figure(figsize=(6,4))   #Tamanho do gráfico

plt.scatter(
    x, y,
    s=tamanho,
    c=cores
)
plt.xticks(np.arange(1.5, 5.1, 0.5)) #Limites do eixo x - De 1.5 a 5: de 0.5 em 0,5
plt.yticks(range(20, 61, 10))  #Limites do eixo y - De 20 a 60: de 10 em 10.

plt.show()

'''

# =======================================================================================================
#                 ===================  GRÁFICO DE BARRA ============================
# =======================================================================================================

'''

import matplotlib.pyplot as plt
import numpy as np
x=['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
y=[10,8,6,4,2,1]

plt.figure(figsize=(10,6))
plt.bar(x,y, color='mediumstaleblue', edgecolor='darkblack', linewitdh=.6)
plt.ylabel('Usage')
plt.title('Programming Language Usage')
plt.ylim(0,10)
plt.show()

'''