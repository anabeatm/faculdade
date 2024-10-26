# Faça um programa que peça para o usuário informar o tamanho de um vetor. 
# Em seguida, crie este vetor e preencha ele com números digitados pelo usuário. 
# Por fim, apresente na tela os números digitados.
tamanhoVetor = int(input("Informa o tamanho do vetor: "))
vetor = [0] * tamanhoVetor
for i in range(0, len(vetor)):
    vetor[i] = int(input(f"Digite o {i+1}° valor do vetor: "))
print(vetor)