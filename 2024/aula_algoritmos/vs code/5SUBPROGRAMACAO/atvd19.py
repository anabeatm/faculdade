# Elabore uma função chamada fatorial que receba um número inteiro positivo como parâmetro 
# e retorne o fatorial deste número.

def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Fatorial de: "))
print(fatorial(numero))