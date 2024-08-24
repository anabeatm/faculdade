# Crie um vetor com 4 números decimais (ponto-flutuante) de modo que o usuário do programa vá digitar esses valores.
vetor4 = [0.0] * 4

vetor4[0] = float(input("Informe um número flutuante: "))
vetor4[1] = float(input("Informe outro número flutuante: "))
vetor4[2] = float(input("Informe um número flutuante: "))
vetor4[3] = float(input("Informe outro número flutuante: "))

print(vetor4)
# a)
soma = vetor4[0] + vetor4[1] + vetor4[2] + vetor4[3]

print(f"> A soma de todos os valores é: {soma}")
# b)
media = soma / len(vetor4)

print(f"> A média dos valores é: {media}")
# c)
multiplicacao = vetor4[0] * vetor4[1] * vetor4[2] * vetor4[3]

print(f"> A multiplicação dos valores é: {multiplicacao}")
# d)
maiorQueMil = 0
if(vetor4[0]>1000):
    maiorQueMil+=1
if(vetor4[1]>1000):
    maiorQueMil+=1
if(vetor4[2]>1000):
    maiorQueMil+=1
if(vetor4[3]>1000):
    maiorQueMil+=1

print(f"> Há {maiorQueMil} números maiores que mil.")

# g) h)
maiorNumero = 0
indiceMaior = 0
if(vetor4[0] >= maiorNumero):
    maiorNumero = vetor4[0]
    indiceMaior = 0
if(vetor4[1] >= maiorNumero):
    maiorNumero = vetor4[1]
    indiceMaior = 1
if(vetor4[2] >= maiorNumero):
    maiorNumero = vetor4[2]
    indiceMaior = 2
if(vetor4[3] >= maiorNumero):
    maiorNumero = vetor4[3]
    indiceMaior = 3

print(f"O maior número é: {maiorNumero}.\nE o maior indicie do vetor é [{indiceMaior}]")
