#Continue o exercício anterior e crie mais variáveis para armazenar (uma para cada): 
#sua idade, seu peso, sua altura e sua data de nascimento. 
#Por fim, apresente todos esses dados na tela dentro de um print só.
nome = input("Escreva seu nome: ")
sobrenome = input("Escreva seu sobrenome: ")
idade = int(input("Qual sua idade? "))
peso = float(input("Qual seu peso? "))
altura = int(input("Qual sua altura em cm? "))
data_nasc = input("Me diga sua data de nascimento. Exemplo: 00/00/0000. ")
print("Bem-vinde", nome, sobrenome, f"! Sua data de nascimento é {data_nasc}, ou seja, você tem {idade} anos.")
print(f"Seu peso é {peso} kg e sua altura é {altura} cm.")
