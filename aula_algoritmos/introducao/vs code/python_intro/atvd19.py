# Tendo como dados de entrada a altura e peso de uma pessoa, construa um algoritmo que
# calcule seu IMC, usando a seguinte fórmula: imc = peso ÷ altura²
altura = int(input("Me diga sua altura em cm: "))
peso = float(input("Me diga seu peso em kg: "))

imc = peso / (altura**2)
new_imc = imc * 10000 # Multiplicando por 10000 para obter o IMC em uma escala de 1m^2 para 1cm^2.
# O valor exato pode variar devido à precisão dos cálculos de ponto flutuante em Python.
new_imc_round = round(new_imc, 1) # Usando a função round() para se obter o arredondamento do número para 1 casa decimal.

print(f"Seu IMC é {new_imc_round}.")
