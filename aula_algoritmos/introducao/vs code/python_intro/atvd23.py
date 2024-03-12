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

imposto_renda = 
