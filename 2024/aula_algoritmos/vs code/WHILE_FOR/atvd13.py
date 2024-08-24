# Utilizando o laço de repetição for, faça um programa que apresente as tabuadas do X a Y 
# para um número informado pelo usuário (semelhante ao anterior, porém o usuário precisa informar três números).
x = int(input("Informe um começo: "))
y = int(input("Informe um final: "))
numTabu = int(input("Agora um número pra tabuada: "))

tabuada = 0

for c in range(x, y):
    tabuada = numTabu * c
    print(f"{c} x {numTabu} = {tabuada}")
