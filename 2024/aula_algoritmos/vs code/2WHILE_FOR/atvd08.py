# Faça um programa que leia 5 números e informe apenas o maior número.
maiorNum = 0

for c in range(5):
    num = int(input("Infome um número: "))
    if(num > maiorNum): 
        maiorNum = num # se num for maior que maiorNum, então maiorNum é atualizado para num
print(f"O maior número é:", maiorNum)
