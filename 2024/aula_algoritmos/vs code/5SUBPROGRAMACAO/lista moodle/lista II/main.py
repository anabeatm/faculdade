import funcoes as f

tam = int(input("Tamanho vetor: "))
# nomes = [""] * tam
# notas = [0.0] * tam
# for i in range(0, tam):
#     nomes[i] = input(f"Nome do {i + 1}° aluno: ")
#     notas[i] = float(input(f"Nota do {i + 1}° aluno: "))
# resultado = f.verificarNotasAbaixoDaMedia(notas, nomes)
# print(f"Os alunos abaixo da média são {resultado}.")

codigos = [""] * tam
quantidades = [0.0] * tam
precos = [0.0] * tam

for i in range(0, tam):
    codigos[i] = input(f"Coloque o código do {i + 1}° produto: ")
    quantidades[i] = float(input(f"Coloque a quantidade do {i + 1}° produto: "))
    precos[i] = float(input(f"Coloque o preço do {i + 1}° produto: "))

resultado = f.calcularValorEstoque(codigos, quantidades, precos)
print(f"O valor total dos produtos são: R${resultado}")