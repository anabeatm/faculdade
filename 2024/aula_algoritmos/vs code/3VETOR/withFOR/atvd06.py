# Crie um vetor para armazenar alguns números que serão utilizados no cálculo da tabuada.
vetor = [25, 1, 74, 6, 47, 28]

# a) Apresente todos os números informados e seu respectivo dobro.

# for i in range(0, len(vetor)):
#     dobro = vetor[i] * 2
#     print(f"{vetor[i]} * 2 = {dobro}")

# b) Para cada número presente no vetor, faça a tabuada do 1 ao 10 para ele 
# (utilizando laço de repetição você vai criar uma tabuada para cada valor do vetor).
for i in range(0, len(vetor)):
    print(f"\nTabuada do {vetor[i]}:")
    for tabuada in range(1, 11):
        resultado = vetor[i] * tabuada
        print(f"{vetor[i]} x {tabuada} = {resultado}")