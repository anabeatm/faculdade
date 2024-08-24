"""Crie um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles 
estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar 
quando for lido um número negativo. No final, apresente quantos números há em cada intervalo.
"""
cont_0_25 = 0
cont_26_50 = 0
cont_51_75 = 0
cont_76_100 = 0

while True:
    numeroPositivo = int(input("Informe um número entre 0 - 100: "))

    if(numeroPositivo > 0 and numeroPositivo <= 25):
        cont_0_25 += 1
    elif(numeroPositivo > 25 and numeroPositivo <= 50):
        cont_26_50 += 1
    elif(numeroPositivo > 50 and numeroPositivo <= 75):
        cont_51_75 += 1 
    elif(numeroPositivo > 75 and numeroPositivo <= 100):
        cont_76_100 += 1

    else:
        if(numeroPositivo < 0):
            break

print(f"Há {cont_0_25} número(s) entre [0 - 25].")
print(f"Há {cont_26_50} número(s) entre [26 - 50].")
print(f"Há {cont_51_75} número(s) entre [51 - 75].")
print(f"Há {cont_76_100} número(s) entre [76 - 100].")