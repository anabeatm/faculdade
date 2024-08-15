#  Faça um programa que peça dois números e imprima na tela somente o maior deles.
x = float(input("Digite um valor: "))
y = float(input("Digite outro valor: "))

x_maior_y = x > y
y_igual_x = y == x

if(x_maior_y):
    print(f"{x} eh maior que {y}.")
# elif(y_igual_x):
#     print(f"{x} eh igual que {y}.")
else:
    print(f"{y} eh maior que {x}.")
