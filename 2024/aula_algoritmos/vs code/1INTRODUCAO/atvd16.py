#Faça um programa que peça a medida do lado de um quadrado, calcule e mostre sua área. Em
# seguida, mostre também o perímetro do quadrado para o usuário.
lado = float(input("Insira o lado de um quadrado: "))

area = lado**2
perim = lado*4

print(f'A área do quadrado {lado}, é {area} e seu perímetro é {perim}.')
