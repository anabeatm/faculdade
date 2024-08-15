# Faça a multiplicação dos números de 1 a j (fatorial) 
# e mostre o resultado final. Exemplo: Se j = 5 você deve calcular 1 * 2 * 3 * 4 * 5 = 120
j = int(input("Informe o valor de j para calcular seu fatorial: "))

fatorial = 1

for c in range(1, j+1, 1):
    fatorial *= c
    print(c)

print(fatorial)
