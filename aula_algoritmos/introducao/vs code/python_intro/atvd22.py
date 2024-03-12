# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em 
# latas de 18 litros, que custam R$120,00. O programa deve informar ao usuário a quantidade de latas de 
# tinta a serem compradas e o preço total.
import math

area_pintar = float(input("Digite o tamanho em metros quadrados da área a ser pintado: "))

litros_necessarios = area_pintar / 3
latas_necessarias = math.ceil(litros_necessarios / 18)
precoTotal = latas_necessarias * 120

print(f"Quantidade total de latas necessárias: {latas_necessarias}.")
print(f"Preço total: {precoTotal:.2f}")
