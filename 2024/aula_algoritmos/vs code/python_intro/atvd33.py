# Faça um programa que peça um número inteiro ao usuário. Se ele for maior do que zero e
#  menor que 100, apresente a mensagem “Número no intervalo definido”, se não, apresente
#  “Número fora do intervalo!”.
num = int(input("Insira um número inteiro: "))
intervalo = 0 < num < 100

if(intervalo):
    print(f"O número {num} está no intervalo definido.")
else:
    print(f"O número {num} não esta no intervalo definido.")
