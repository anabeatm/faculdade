# INTRO

# criando uma string com várias letras, para nossos testes..
#%%
letras = 'abcdefghijklmnopqrstuvwxyz@#*+'

# criando uma lista de letras
lista = list(letras)
print('len(lista):', len(lista))
print(lista)

# importando a biblioteca matemática: numpy
import numpy as np

# transformando nossa lista em um array do numpy
lista = np.array(lista)


# Imprime o tamanho (número total de elementos) da lista ou array
print('tamanho:', len(lista))

# Imprime o "shape" (formato) do array: número de linhas e colunas, se for um array NumPy.
# Isso funciona apenas se 'lista' for um array NumPy; se for uma lista comum, causará erro.
print('shape:', lista.shape)

# Imprime a quantidade de dimensões do array (1D, 2D, etc.)
# Também só funciona se 'lista' for um array NumPy.
print('ndim:', lista.ndim)

# Imprime a lista ou array original
print('lista:', lista)

# Imprime a lista ou array na ordem reversa (do último para o primeiro elemento)
print('lista-reverso:', lista[::-1])



# dado a lista anterior, faça os exercícios:

# 1- capturar os primeiros 10 elementos e imprimir na tela
# %%
print(lista[:10:])
# 2- capturar os últimos 10 elementos e imprimir na tela
#%%
print(lista[20::])
# 3- capturar os 10 elementos do meio e imprimir na tela
#%%
tamanho = len(lista)
meio = tamanho // 2
print(lista[meio-5:meio+5:])
#%%
# 4- imprimir o 21o elemento apenas
print(lista[21])
#%%
# 5- imprimir todos elementos, menos os 5 últimos
print(lista[:-5])
#%%
# 6- imprimir todos elementos do início até o meio
print(lista[:meio])
# 7- imprimir todos elementos do meio até o final
#%%
print(lista[meio:])
#%%
# 8- imprimir todos elementos a partir do 5 , menos os 5 últimos
print(lista[5:-5])
#%%
# 9- imprimir o 12 elemento
print(lista[12])
#%%
# 10- fazer um laço que repita 10 vezes, imprimindo cada vez 3 elementos
for i in range(10):
    print(lista[i*3:(i*3) + 3])
    
#%%
#tabela = lista.reshape((5,6))
#tabela = lista.reshape((3,3))
#tabela = lista.reshape((2,-1))
tabela = lista.reshape((-1, 2)) # linha, coluna
print(tabela)
print('shape:', tabela.shape)
print('ndim:', tabela.ndim)

print(tabela)
    
print('-- linhas:')
for linha in tabela:
    print(linha)

print('\n-- colunas:')
for coluna in tabela.T: # aqui, o T significa transpose..
    print(coluna)


# EXERCICIOSSSS....
#%%
# 11- verificar o que significa 'TRANSPOSE' na internet
    # linha vira coluna e coluna vira linha
print(tabela)
print(tabela.T)
#%%
# 12- fazer o transpose da tabela e armazenar em outra variável: tabela_t
#       imprimir a tabela normal e sua transposta
# tabela = np.matrix([['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
#                      ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
#                      ['u', 'v', 'w', 'x', 'y', 'z', '@', '#', '*', '+']])         
#tabela_t = ??

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z', '@', '#', '*', '+']
print(lista)

lista = np.array(lista)
lista = lista.reshape(-1, 10)
listaT = lista.T
print(lista)

# print('Tabela', tabela)
# print('Tabela Transposta',tabela_t)
#%%
# 13- capturar da tabela o elemento linha=2 e coluna=3, e imprimir na tela
result = lista[2][3]
print(result)
#%%
# 14- transformar a tabela em um shape (10, 3), armazenar em tabela2. 
#       Imprimir cada linha da tabela2
#       Comparar o resultado com a pergunta: 
tabela2 = lista.T # são 10 colunas e 3 linhas, com o .T vira 90°

for linha in tabela2:
    print('linha: ', linha)


# tabela2 = ??
# for linha in tabela2:
#     print(linha)
# print('Quantidade de linhas da tabela 2:', ??)
#%%
# 15- imprimir as colunas da tabela2
for coluna in tabela2.T:
    print('coluna:', coluna)
#%%
#16- capturar da tabela, os elementos do meio, e colocar na variável: tabela3
#       Imprimir a tabela3. Abaixo o que deve aparecer:
#       ['h' 'i' 'j' 'k']
#       ['n' 'o' 'p' 'q']
#       ['t' 'u' 'v' 'w']
tabela3 = lista[1: -1, 1: -1]
print(tabela3)

# tabela3 = tabela[ ?? ]
# print('Tabela 3',tabela3)
#%%
tabela4 = lista.reshape(-1, 5)
print(tabela4[1: -1, 1: -1])
#%%
# 17- imprimir o shape da tabela3
print('Shape 3:',tabela3.shape)
print("Shape 4:", tabela4.shape)
#%%
# 18- imprimir todas colunas da tabela3
tabela3_t = ??
print('Colunas tabela 3', tabela3_t)
#%%
# 19- transformar a tabela 3 em uma lista, e colocar dentro da variável: lista3
#       imprimir a lista3
lista3 = tabela3.tolist() # função da biblioteca numpy
print('Transformando tabela 3 em lista 3: ', lista3)
print('-' * 10)
lista4 = tabela4.tolist()
print(lista4)

#%%
lista4 = tabela4.flatten()
print(lista4)
#%%
# 20- imprimir na tela, da lista3, os elementos de índice: 1, 4, 7 e 8




# %%
# anotação aula 27/05
lista3 = [item for sublist in lista3 for item in sublist]
print(lista3)
# %%
