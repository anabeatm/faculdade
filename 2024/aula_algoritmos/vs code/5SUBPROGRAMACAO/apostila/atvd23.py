"""Elabore  um  programa  que  contenha  uma  rotina  que  receba  três  notas  de  um  aluno  como 
parâmetros e uma letra. 
Se a letra for A, a rotina deverá calcular a média Aritmética das notas do aluno.
Se a letra for P, a rotina deverá calcular a média Ponderada (com pesos 5, 3 e 2).
A média deverá ser retornada ao programa principal para, então, ser mostrada.

Caso a letra seja diferente de A ou P, a rotina deverá retornar -1"""

def rotinaNotasdoAluno(notas, letra):
    if(letra == "a"):
        soma = 0
        for c in range(0, len(notas)):
            soma += notas[c]
        media = soma / len(notas)
        return media
    elif(letra == "p"):
        media = ( (notas[0] * 5) + (notas[1] * 3) + (notas[2] * 2) ) / ( 5 + 3 + 2)
        return media
    else:
        return "-1"


notas = [0.0] * 3
for i in range(0, 3):
    notas[i] = float(input(f"{i + 1}° nota: "))
letra = input("Qual média gostaria de calcular? Média Aritmética [A] ou Média Ponderada [P]: ").lower()
resultado = rotinaNotasdoAluno(notas, letra)
print(resultado)