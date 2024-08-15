# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
# no dia. Calcule e mostre quanto você ganhou no dia e o total do seu salário em um mês
# (considerando 30 dias).
ganho_horas = float(input('Quanto você ganha por hora? R$'))
horas_dia = int(input("Quanto você trabalha por dia? "))

ganho_dia = ganho_horas * horas_dia
ganho_mes = ganho_dia * 30

print(f"Você ganha por dia {ganho_dia} reais. Ao final do mês, seu salário é R${ganho_mes}.")
