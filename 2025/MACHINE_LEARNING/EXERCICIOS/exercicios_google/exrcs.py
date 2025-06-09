#%%
"""1. VOGAIS: Faça um programa que conte o número de vogais em uma string.
Sabemos que as strings se comportam como um array de caracteres.

Sabendo disso você fará um programa que capture uma string qualquer (pode ser uma frase com várias palavras).

Capture esta string em uma variável.

Faça um loop de repetição para cada letra desta string.

Caso a letra seja uma vogal, que você some 1 em uma variável contador.

Ao final do programa, imprima a contagem das vogais."""
frase = input("Digite uma frase: ")

cont = 0

for vogal in frase:
  if(vogal in 'aeiou'):
    cont += 1

print('total de vogais: ', cont)

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
lista = []
listaPositivos = []
listaNegativos = []
somaPos = 0
somaNeg = 0
contPos = 0
contNeg = 0

while(True):
  numero = int(input('Digite um número (neg/pos): '))
  if(numero == 0):
    break
  lista.append(numero)

print("lista geral: ", lista)

for numero in lista:
  if(numero > 0):
    listaPositivos.append(numero)
    somaPos += numero
    contPos += 1
  else:
    listaNegativos.append(numero)
    somaNeg += numero
    contNeg += 1

if listaPositivos:
  print("lista dos positivos: ", listaPositivos)
  print("soma total dos positivos: ", somaPos)
  print("total dos positivos: ", contPos)
  print("media dos positivos: ", somaPos / contPos)
else:
  print("nenhum positivo")

if listaNegativos:
  print("lista dos negativos: ", listaNegativos)
  print("soma total dos negativos: ", somaNeg)
  print("total dos negativos: ", contNeg)
  print("media dos negativos: ", somaNeg / contNeg)
else:
  print("nenhum negativo")

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
cardapio = {
    "lanches": {
        "hamburguer": 12.50,
        "cheeseburguer": 14.00,
        "x-bacon": 16.50,
        "cachorro-quente": 10.00,
        "veggie burguer": 15.00
    },
    "bebidas": {
        "refrigerante": 5.00,
        "suco": 6.50,
        "agua": 3.00
    }
}

for categoria, itens in cardapio.items():
  print(categoria)
  for nome, preco in itens.items():
    print(nome, " --> R$", preco)

pedidos = []
soma = 0


while True:
  
  existe = False

  pedido = input("Digite o que deseja: ").lower()
  if(pedido == "0"):
    break

  for tipo, item in cardapio.items():
    for nome, preco in item.items():
        if(pedido == nome):
          pedidos.append(pedido)
          soma += preco
          existe = True
        
  if not existe:
    print("nao pertence ao cardapio")

print("pedidos --:> ", pedidos)
print("total: R$", soma)

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
placas = [
  "AAA0001",
  "bbb0002",
  "CCC0A00",
  "ddd1B11",
  "eee2233",
  "fff9999",
  "ggg0C22"
]

for placa in placas:
  if(placa[4].isalpha()):
      print(f"{placa} --- placa nova")
  else:
    print(f"{placa} --- placa antiga")

# %%
# entendo diferença entre for x in y e for i in range(n):
numeros = [10, 20, 30, 40]
for numero in numeros:
  print(numero * 2)

for i in range(len(numeros)):
  print(numeros[i] * 2)
# %%
"""Durante nossas aulas fizemos vários exemplos em sala.

Os exemplos se basearam em comandos da linguagem, além do entendimento de listas e dicionários.

Seguindo nossas aulas, vimos que strings são considerados listas de caracteres em python, ou seja, é possível percorrer uma string pegando caracter por caracter.

Sabendo que recentemente no Brasil foram alteradas algumas leis de trânsito e dentre elas foi alterado a utilização uma placa nos carros de maneira diferente. 
Anteriormente tínhamos placas que começavam com 3 letras e depois 4 números, exemplo: ASD5678. Atualmente temos como placas de carros com 3 letras, 1 número, 
uma letra e depois 2 números, exemplo: AFF4S56.

Suponha que você está trabalhando no Detran que captura placas de carros e verifica se o carro está com placa no padrão antigo ou novo. Faça um programa que 
avalie uma string, vindo de algum sistema de reconhecimento de imagens, e diga se esta string se refere à placa antiga ou placa nova.

Seu sistema deverá avaliar um dicionário de dados onde é colocado o cpf da pessoa como 'chave' e a placa como 'valor'.

As placas que você deverá conferir são: AAA0001, bbb0002, CCC0A00, ddd1B11, eee2233, fff9999, ggg0C22.

Você deverá colocar os valores das placas em um dicionário de dados. Deverá tambémd efinir como chave deste dicionário um número fictício de cpf que contenha 11 dígitos.

Após criar seu dicionário, você fará um loop de repetição capturando cada elemento deste dicionário e verificando se a placa é antiga ou nova. 
Ao final do seu loop você deverá imprimir na tela: 1) o número da placa 2) o cpf da pessoa que tem esta placa 3) indicar se o tipo da placa é antiga ou nova.

Veja um exemplo de saída do software: AAA0001 -- 01234567899 -- placa antiga CCC0A00 -- 98765432100 -- placa nova

Dentro do seu loop principal, você deverá criar um outro loop que irá verificar cada um dos caracteres da placa e conferir se segue o modelo de placa novo ou antiga."""
placas = {
  'AAA0001' : '038.921.467-80',
  'bbb0002' : '571.264.930-20',
  'CCC0A00' : '403.195.782-56',
  'ddd1B11' : '120.648.395-77',
  'eee2233' : '846.370.219-04',
  'ggg0C22' : '695.208.134-98'
}

for placa, cpf in placas.items():
  if(placa[4].isalpha()):
    print(placa, " --- ", cpf, "---> placa nova")
  else:
    print(placa, " --- ", cpf, "---> placa antiga")

# %%
