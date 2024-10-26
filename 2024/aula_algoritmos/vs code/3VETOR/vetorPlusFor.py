# numeros = [1, 2, 3, 4, 5, 6]

# vetor = [0] * len(numeros)

# for i in range(0, len(numeros)):

#     if(numeros[i] % 2 == 0):

#         vetor[i] = "par"

#     else:

#         vetor[i] = "impar"
# print(vetor)

# v = ["maçã", "abacaxi", "melancia", "uva"]

# for i in range(0, len(v)):
#     print(v[i])

# v = ["maçã", "abacaxi", "melancia", "uva"]

# for valor in range(len(v)):
#     print(valor)

# v = [10, 20, 30, 40]
# print(v)

# v[2]=  5
# print(v)

# vet = [1, 2, 3, 4]
# print(vet[4])

# x = [0] * 10

# while(x[5] < 10 or x[5]>20 ):

#     x[5] = int(input("Informe um valor:"))    

# print("Valor informado:", x[5])

# v = [1, 2, 5, 10, 7, 8]

# x = v 

# x[3] = 50

# print(v[3], "e", x[3])

# numeros = [10, 20, 5, 3, 10, 8]

# s = 0 

# for i in range(0, len(numeros)):

#     s = s + numeros[i]

# print(s)

numeros = [10, 20, 50, 30, 10, 15]

s = numeros[0]

for i in range(1, len(numeros)):

    if(numeros[i] > s):

        s = numeros[i]
        print(s)