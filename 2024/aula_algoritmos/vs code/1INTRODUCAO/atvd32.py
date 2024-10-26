# Faça um programa que peça a idade do usuário. Se ele for maior de idade, peça o salário
#  dele e dê um aumento de 5%, apresentando na tela o valor final do salário. Se ele for
#  menor, informe a mensagem “Cálculo não permitido”.
idade = int(input("Insira sua idade: "))
maioridade = idade >= 18

if(maioridade):
    salario = float(input("Insira seu salário: R$"))
    aumento = salario + (salario * 0.05)
    print(f"Você recebeu um aumento de 5% em seu salário de R${salario} para R${aumento}.")
else:
    print("Cálculo não realizado.")
