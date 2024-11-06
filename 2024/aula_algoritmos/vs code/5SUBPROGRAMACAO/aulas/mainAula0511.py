import aula0511 as a

tamanho = int(input("Digite o tamanho do vetor: "))
tipo = input("Digite o tipo do vetor (int, float): ")
vetor = a.gerarVetor(tamanho, tipo)
print(vetor)

a.ordenarBolha(vetor)
print(f"O vetor ordenado é: {vetor}")
a.exibirDados(vetor)