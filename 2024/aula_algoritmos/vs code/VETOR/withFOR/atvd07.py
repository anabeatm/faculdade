# Maria está organizando um chá de bebê e precisa fazer a lista de convidados. 
# Ela gostaria de saber quantas pessoas irão comparecer ao evento. 
# Crie um algoritmo que solicite ao usuário que digite o número de convidados e, 
# em seguida, armazene a quantidade em uma variável. Utilize um laço de repetição para pedir o 
# nome de cada convidado e armazená-lo em um vetor. Ao final, exiba a quantidade de convidados.

qntdConvidados = int(input("Informa quantos convidados será: "))
nomeConvidados = [""] * qntdConvidados

for i in range(0, len(nomeConvidados)):
    nomeConvidados[i] = input("Informa o nome dos convidados: ")
    
print(f"Os convidados são: {nomeConvidados}")