# Faça a soma dos números de X a Y (informados pelo usuário), 
# desde que X seja menor que Y, e apresente o valor total (semelhante ao anterior).
x = int(input("Informe o valor de x: "))
y = int(input("Informe o valor de y: "))

soma = 0

if(x < y):
    for c in range(x, y, 1):
        soma += c
    print(soma)
else:
    print("Valor inválido. Tente novamente.")