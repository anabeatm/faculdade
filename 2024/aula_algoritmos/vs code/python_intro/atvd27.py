# Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100).
#  Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, se não,
#  “Reprovado”.
trabalho = int(input("Digite sua nota do trabalho (0 a 100): "))
prova = int(input("Digite sua nota da prova (0 a 100):" ))

media = (trabalho + prova) / 2

if(media >= 60):
    print("Aprovado.")
else:
    print("Reprovado.")
