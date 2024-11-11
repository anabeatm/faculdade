"""
Implemente uma rotina chamada fatorial que receba um valor inteiro como parâmetro e retorne 
o fatorial deste número. Implemente também uma rotina chamada calcularS que receba como parâmetro um 
valor inteiro e positivo N e retorne o valor de S, obtido pelo seguinte cálculo:

𝑆= 1 + 1/1! + 1/2! + 1/3! + ⋯ + 1/𝑁!

Solicite o valor de N e apresente o valor de S no programa principal. 
"""
def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def calcularS(numeroN):
    if(numeroN < 1):
        return "Valor deve ser positivo"
    
    s = 1
    fatorial = 1
    i = 1

    while(i <= numeroN):
        fatorial *= i
        s = s + 1 / fatorial
        i += 1
    
    return s

numero = int(input("Digite um valor para seu fatorial: "))
print(fatorial(numero))
numeroN = int(input("Digite um valor positivo para N: "))
print(f"{calcularS(numeroN):.2f}")