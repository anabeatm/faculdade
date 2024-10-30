# Implemente uma função que receba nos parâmetros um vetor numérico. A função deverá
# retornar ao programa principal o número de valores pares presentes neste vetor.


def vetorPar(vetor):
    cont = 0
    for i in range(0, len(vetor)):
        if(vetor[i] % 2 == 0):
            cont = cont + 1
    return cont
        

vetor = [15, 87, 109, 28, 49, 36, 59]
# qntd_par = vetorPar(vetor)
print("Quantidade de pares:", vetorPar(vetor))
