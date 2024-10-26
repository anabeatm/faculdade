#  Faça um programa que peça um número e informe se este número é múltiplo de 3.
num = float(input("Digite um número: "))
print("Irei verificar se ele é múltiplo de 3...")

if(num % 3 == 0):
    print(f"O número {num} é múltiplo de 3.")
else:
    print(f"O número {num} não é múltiplo de 3.")
