# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# #Calcule e mostre o total do seu salário no referido mês (salário bruto), 
# sabendo-se que são descontados 7.5% para o Imposto de Renda, 8% para o INSS e 1% para o sindicato. 
# Faça um programa que nos dê:
# salário bruto.
# quanto pagou de imposto de renda (calcule sobre o salário bruto).
# quanto pagou ao INSS (calcule sobre o salário bruto).
# quanto pagou ao sindicato (calcule sobre o salário bruto).
# o salário líquido (o que sobrou após os descontos).
ganha_hora = float(input("Digite quanto você recebe por hora: R$"))
horas_mes = int(input("Digite quantas horas você trabalha por mês: "))

salarioBruto = ganha_hora * horas_mes
print(f"Salário bruto: R${salarioBruto}")

imposto_renda = salarioBruto * (7.5 / 100)
print(f"Imposto de renda: {imposto_renda:.2f}")

inss = salarioBruto * (8 / 100)
print(f"INSS: {inss}")

sindicato = salarioBruto * (1 / 100)
print(f"Sindicato: {sindicato}")

salarioLiquido = salarioBruto - (imposto_renda + inss + sindicato)
print(f"Salário líquido: {salarioLiquido:.2f}")
