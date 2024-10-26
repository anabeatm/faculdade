#  Faça um programa que peça a idade do usuário. Se ele for maior de idade, peça para ele
#  digitar o nome dele e informe a mensagem “Bem vindo Fulano”. Caso contrário, apresente
#  “Entrada não permitida”.
idade = int(input("Insira sua idade: "))
maioridade = idade >= 18

if(maioridade):
    nome = input("Insira seu nome: ")
    print(f"Bem-vinde, {nome}!")
else:
    print("Entrada negada.")

