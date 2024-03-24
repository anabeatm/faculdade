# Faça um programa que verifique o sexo de uma pessoa. O usuário deve informar ‘F’ ou ‘M’
#  e oprograma deve escrever “Feminino” ou “Masculino”, conforme a letra digitada.
sexoBiologico = input("Digite seu sexo designado ao nascer [F/M]: ").upper()

if(sexoBiologico == "F"):
    print("Feminino.")
if(sexoBiologico == "M"):
    print("Masculino.")
if(sexoBiologico != "F" and "M"):
    print("Tente novamente.")

print("Fim do programa.")
