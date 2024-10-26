# Utilizando o laço de repetição for, faça um programa que apresente 
# as tabuadas do 1 ao 10 para um número informado pelo usuário.
numTabuada = int(input("Informe um número para gerar sua tabuada de 1 a 10: "))

tabuada = 0 # contador da tabuada

for c in range(1, 11): # iniciando o loop de 1 a 10
    tabuada = c * numTabuada # o resultado da tabuada será o loop de `c` multiplicado pelo n° informado pelo usuário

    print(f"{c} x {numTabuada} = {tabuada}") # saída
