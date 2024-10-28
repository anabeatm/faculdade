# Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = [""] * 5

while(True):
    perguntas[0] = input("Telefonou para a vítima? [s/n] ")
    perguntas[1] = input("Esteve no local do crime? [s/n] ")
    perguntas[2] = input("Mora perto da vítima? [s/n] ")
    perguntas[3] = input("Devia para a vítima? [s/n] ")
    perguntas[4] = input("Já trabalhou com a vítima? [s/n] ")
    sair = input("Sair do programa? [sim/não]: ")
    if(sair == "sim"):
        break
    else:
        continue

cont = 0
for i in range(0, len(perguntas)):
    if(perguntas[i] == "s"):
        cont += 1

if(cont == 5):
    print("Assasino!")
elif(3 <= cont <= 4):
    print("Cúmplice!")
elif(cont == 2):
    print("Suspeito!")

else:
    print("Inocente.")
