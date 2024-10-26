# Faça um programa que leia três valores: A, B, C. Em seguida, verifique se a soma de A +
#  B é maior que C. Se for, apresente “A+B é maior que C”. Se não, apresente “C é maior que
#  todos!”.
a = float(input("Digite um número a: "))
b = float(input("Digite um número b: "))
c = float(input("Digite um número c: "))

soma = a + b

if (soma > c):
    print(f"A soma entre {a} e {b} é maior que {c}.")
else:
    print(f"{c} é maior que todos!")
