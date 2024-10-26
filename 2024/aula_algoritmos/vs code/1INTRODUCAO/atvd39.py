# Faça um algoritmo que peça um número inteiro para o usuário. Se esse número for par,
#  some ele + 5, se não, multiplique o número por 2.
num = int(input("Digite um número: "))
par = num % 2 == 0

if(par):
    maisCinco = num + 5
    print(maisCinco)
else:
    vezesDois = num * 2
    print(vezesDois)
