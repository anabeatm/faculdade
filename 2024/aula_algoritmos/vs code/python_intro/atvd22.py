# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$450,00. 
# O programa deve informar ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
import math

area_pintar = float(input("Digite o tamanho em metros quadrados da área a ser pintado: "))

litros_necessarios = area_pintar / 6 # A quantidade de litros necessários para cobrir toda a área a ser pintada 
# é feita dividindo a área coberta por 6 metros (a cada 1 litro).
latas_necessarias = math.ceil(litros_necessarios / 18) # Como uma lata contém 18 litros, dividimos os litros necessários por 18, logo que é o total de cada lata.
# Arredondando esse valor para que a quantidade mínima seja necessária.
precoTotal = latas_necessarias * 450 # Por último calculamos o valor total mutiplicando a quantidade de latas total pelo preço de cada lata.

print(f"Quantidade total de latas necessárias: {latas_necessarias}.")
print(f"Preço total: {precoTotal:.2f}")
