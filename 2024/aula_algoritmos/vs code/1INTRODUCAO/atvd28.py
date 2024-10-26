#  Faça um programa que peça ao aluno o conceito dele na disciplina (A, B, C ou D). Se o
#  conceito for A, B ou C apresente “Aprovado”, se não, apresente “Reprovado”.
concUsu = input("Digite seu conceito na disciplina: ").upper()
# conc = "A" == "B" == "C"

if(concUsu == "A"):
    print("Aprovado.")
elif(concUsu == "B"):
    print("Aprovado.")
elif(concUsu == "C"):
    print("Aprovado.")

else:
    print("Reprovado.")
