#  Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
num = float(input("Digite um valor: "))
positivo = num > 0 # criando a comparação antes por casualidade.
if(positivo):
    print(f"O valor {num} é positivo.")
else:
    print(f"O valor {num} é negativo.")