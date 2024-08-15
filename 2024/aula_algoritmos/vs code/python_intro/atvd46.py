# Construa um programa que receba três valores, A, B e C. Em seguida, apresente na tela
#  somente o maior deles.
a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
c = float(input("Insira o valor de C: "))

if(a > b and a > c):
    print('A é maior.')

elif(b > a and b > c):
    print('B é maior.')

else:
    print('C é maior.')
