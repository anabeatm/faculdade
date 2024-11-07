"""Exercício 1: Análise de Notas de Estudantes

Contexto: Uma escola quer calcular a média das notas dos alunos de uma turma e identificar se algum aluno obteve uma nota abaixo da média. 
Crie uma função que calcule a média das notas de todos os alunos e, em seguida, retorne uma lista com o nome dos alunos cujas notas estão 
abaixo da média.

Enunciado: Crie uma função verificar_notas_abaixo_da_media(notas, nomes) que recebe duas listas:
notas: uma lista com as notas dos alunos.
nomes: uma lista com os nomes dos alunos.
A função deve calcular a média das notas e retornar uma lista com os nomes dos alunos cujas notas estão abaixo da média.

Exemplo de uso:

notas = [7, 4, 9, 6, 5]
nomes = ["João", "Maria", "Pedro", "Ana", "Lucas"]
print(verificar_notas_abaixo_da_media(notas, nomes))

# Saída esperada: ['Maria', 'Ana', 'Lucas']
"""
def verificarNotasAbaixoDaMedia(notas, nomes):
    soma = 0
    index = 0
    abaixoDaMedia = [""] * len(notas)

    for i in range(0, len(notas)):
        soma += notas[i]

    media = soma / len(notas)
    
    for c in range(0, len(notas)):
        if(notas[c] < media):
            abaixoDaMedia[index] = nomes[c]
            index += 1

    return abaixoDaMedia[:index]

"""Exercício 2: Controle de Estoque de Produtos

Contexto: Uma loja de eletrônicos possui um sistema de controle de estoque onde cada produto tem um código, uma quantidade em estoque 
e um preço unitário. O gerente quer saber o valor total em estoque para cada produto.

Enunciado: Crie uma função calcular_valor_estoque(codigos, quantidades, precos) que recebe três listas:
codigos: uma lista com os códigos dos produtos.
quantidades: uma lista com as quantidades em estoque para cada produto.
precos: uma lista com os preços unitários de cada produto.
A função deve retornar uma lista com o valor total em estoque para cada produto (quantidade * preço unitário).

Exemplo de uso:

codigos = ["A001", "A002", "A003"]
quantidades = [10, 5, 8]
precos = [200.0, 150.0, 120.0]
print(calcular_valor_estoque(codigos, quantidades, precos))

# Saída esperada: [2000.0, 750.0, 960.0]
"""

def calcularValorEstoque(codigos, quantidades, precos):
    valorTotal = [0] * len(codigos)
    index = 0

    for i in range(0, len(codigos)):
        valorTotal[index] = quantidades[i] * precos[i]
        index += 1
    
    return valorTotal[:index]

"""Exercício 3: Análise de Temperaturas em Diferentes Cidades

Contexto: Uma estação meteorológica registra as temperaturas médias diárias de diferentes cidades. 
O analista quer saber quantos dias a temperatura foi superior a uma certa referência em cada cidade.

Enunciado: Crie uma função dias_acima_referencia(temperaturas, referencia) que recebe duas listas:
temperaturas: uma lista com as temperaturas médias diárias de uma cidade durante uma semana (7 dias).
referencia: um número que representa a temperatura de referência.
A função deve retornar o número de dias em que a temperatura foi superior à referência.

Exemplo de uso:

temperaturas = [30, 32, 35, 28, 33, 31, 30]
referencia = 31
print(dias_acima_referencia(temperaturas, referencia))

# Saída esperada: 4
"""

def diasAcimaReferencia(temperaturas, referencia):
    acimaReferencia = [0] * len(temperaturas)
    index = 0

    for i in range(0, len(temperaturas)):
        if(temperaturas[i] >= referencia):
            acimaReferencia[index] = temperaturas[i]
            index += 1
    
    return len(acimaReferencia[:index])

"""Exercício 4: Gestão de Salários de Funcionários

Contexto: Uma empresa quer saber qual é o salário médio dos seus funcionários e identificar os funcionários que 
ganham acima da média.

Enunciado: Crie uma função salarios_acima_media(salarios, nomes) que recebe duas listas:
salarios: uma lista com os salários dos funcionários.
nomes: uma lista com os nomes dos funcionários.
A função deve calcular a média dos salários e retornar uma lista com os nomes dos funcionários que ganham acima da média.

Exemplo de uso:

salarios = [3000, 2500, 5000, 4000, 3200]
nomes = ["Carlos", "Maria", "Pedro", "Ana", "Luiza"]
print(salarios_acima_media(salarios, nomes))

# Saída esperada: ['Carlos', 'Pedro', 'Ana']
"""
def salariosAcimaMedia(salarios, nomes):
    salariosAcimaMedia = [0.0] * len(salarios)
    index = 0
    soma = 0

    for c in range(0, len(salarios)):
        soma += salarios[c]
    
    mediaSalarial = soma / len(salarios)

    for i in range(0, len(salarios)):
        if(salarios[i] > mediaSalarial):
            salariosAcimaMedia[index] = nomes[i]
            index += 1
    
    return salariosAcimaMedia[:index]