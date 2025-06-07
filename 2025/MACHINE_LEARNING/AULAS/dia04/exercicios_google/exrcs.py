#%%
"""1. VOGAIS: Faça um programa que conte o número de vogais em uma string.
Sabemos que as strings se comportam como um array de caracteres.

Sabendo disso você fará um programa que capture uma string qualquer (pode ser uma frase com várias palavras).

Capture esta string em uma variável.

Faça um loop de repetição para cada letra desta string.

Caso a letra seja uma vogal, que você some 1 em uma variável contador.

Ao final do programa, imprima a contagem das vogais."""

frase = input("Escreva uma frase: ").lower()
cont = 0
for vogal in frase:
  if vogal in "aeiou":
    cont += 1

print(cont)
# %%
"""POSITIVOS E NEGATIVOS: Faça um programa que manipule números positivos e negativos.
Peça para o usuário digitar vários números (positivos e negativos).

Este pedido deve estar dentro de um loop de repetição.

Dentro do loop, você irá capturar todos os números digitados para dentro de uma lista geral.

Quando o usuário digitar o zero, que pare este loop de repetição.

Após isso, faça outro loop de repetição para percorrer esta lista.

Dentro deste loop deve dever ser feito uma comparação se o número é positivo e negativo. 
Caso positivo, coloque o número dentro de uma lista só de números positivos. 
Caso positivo, some o número em uma variável. 
Caso positivo conte +1 em uma variável contador. 
Faça o mesmo para os números negativos.

Ao final seu programa deverá imprimir na tela:
lista geral
lista de positivos
lista de negativos
soma de positivos
soma de negativos
contagem de positivos
contagem de negativos
média de positivos
média de negativos"""
array = []

while True:
  num = int(input("Digite um número: "))
  if(num == 0):
    break
  array.append(num)
  

print(array)


def positivos(array):
  soma = 0
  cont = 0
  arrayPositivos = []
  for positivos in array:
    if(positivos > 0):
      arrayPositivos.append(positivos)
      soma += positivos
      cont += 1
  if not(arrayPositivos):
    print("lista vazia")
  else:
    print("lista de positivos --> ", arrayPositivos)
    print("soma --> ", soma)
    print("média --> ", soma/cont)

def negativos(array):
  soma = 0
  cont = 0
  arrayNegativos = []
  for negativos in array:
    if(negativos < 0):
      arrayNegativos.append(negativos)
      soma += negativos
      cont += 1
  if not(arrayNegativos):
    print('lista vazia')
  else:
    print("lista de positivos --> ", arrayNegativos)
    print("soma --> ", soma)
    print("média --> ", soma/cont)

positivos(array)
negativos(array)
# %%
"""LANCHONETE: Uma lanchonete tem em seu cardápio 5 comidas e 3 bebidas armazenados em um dicionário.
Veja exemplo:

cardapio = {}
cardapio['xbug'] = 7.30

print(cardapio)

saída:
{'xbug': 7.3}

FAÇA:
Preencha o dicionário que representa o cardápio corretamente com o nome e preço de 5 lanches e 3 bebidas

Faça um laço de repetição que mostre na tela (linha por linha) o nome do produto e o preço que você cadastrou.

Depois, supondo que chegou um cliente na loja, capture o nome do lanche e da bebida do cliente.

Busque no dicionário (cardápio) o preço do que o cliente pediu.
Some o valor dos produtos pedidos pelo cliente
Mostre na tela o valor final do pedido."""

cardapio = {'xburger' : 7.30,
            'americano' : 5.80,
            'calabresa' : 8.90,
            'xsalada' : 7.30,
            'xtudo' : 9.99,
            'coca-cola': 3.50,
            'suco' : 2.50,
            'pepsi' : 3.40}


for key, valor in cardapio.items():
  print(key, ' --> R$', valor)

pedidos = {}

while True:
  pedido = input('Faça seu pedido: ').lower()
  if(pedido == "0"):
    break
  if pedido in cardapio:
    if pedido in pedidos:
      pedidos[pedido] += 1
    else:
      pedidos[pedido] = 1

print('-' * 40)
print('pedidos --> ', pedidos)

soma = 0
for item, qntd in pedidos.items():
  preco = cardapio[item]
  subtotal = preco * qntd
  soma += subtotal
print('Total: R$', soma)
# %%
"""Placa trânsito:
Seguindo nossas aulas, vimos que strings são considerados listas de caracteres em python, ou seja, 
é possível percorrer uma string pegando caracter por caracter.

Sabendo que recentemente no Brasil foram alteradas algumas leis de trânsito e dentre elas foi alterado 
a utilização uma placa nos carros de maneira diferente.

Anteriormente tínhamos placas que começavam com 3 letras e depois 4 números, exemplo: ASD5678.

Atualmente temos como placas de carros com 3 letras, 1 número, 1 letra e depois 2 números, exemplo: AFF4S56.

Faça um programa que avalie uma string, vindo de algum sistema de reconhecimento de imagens, e diga se 
esta string se refere à placa antiga ou placa nova.

Seu sistema deverá avaliar uma lista de placas. As placas que você deverá conferir são: AAA0001, bbb0002, 
CCC0A00, ddd1B11, eee2233, fff9999, ggg0C22.

Você fará um loop de repetição capturando cada elemento desta lista e irá verificar se a placa é antiga ou nova.

Ao final do seu loop você deverá imprimir na tela: 1.1. o número da placa 1.1. indicar se o tipo da placa é antiga ou nova.

Veja um exemplo de saída do software:

AAA0001 -- placa antiga
CCC0A00 -- placa nova
Dica: para verificar se uma placa é nova ou antiga, você deverá verificar cada um dos caracteres da placa 
e conferir se segue o modelo de placa nova ou antiga."""
placas = ['AFF4S56', 'CCC0A00', 'ddd1B11', 'eee2233', 'fff9999', 'ggg0C22']

for placa in placas:
  if(placa[4].isalpha()):
    print(placa, ' ---> placa nova')
  else:
    print(placa, ' ---> placa antiga')

#%%
# alternativa:
for i in range(len(placas)):
  if(placas[i][4].isalpha()):
    print(placa, ' ---> placa nova')
  else:
    print(placa, ' ---> placa antiga')

# %%
# entendo diferença entre for x in y e for i in range(n):
numeros = [10, 20, 30, 40]
for numero in numeros:
  print(numero * 2)

for i in range(len(numeros)):
  print(numeros[i] * 2)
# %%
