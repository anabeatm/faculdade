# Importa a biblioteca numpy para cálculos numéricos
import numpy as np

# Comentários explicam o objetivo:
# - Contar quantas classes existem no conjunto de dados
# - Contar quantos registros existem por classe
# - Calcular o desbalanceamento das classes (Índice de Desbalanceamento - IR)

# Fórmula do IR (Índice de Desbalanceamento):
# IR = (quantidade da classe mais frequente) / (quantidade da classe atual)

# Importa a função 'data_set' de outro arquivo chamado 'anotProf'
from anotProf import data_set

# Caminho do arquivo CSV com os dados
fname = r'C:\Users\anabe\faculdade\2025\MACHINE_LEARNING\AULAS\dia04\iris_dataSet.csv'

# Carrega os dados usando a função importada
data = data_set(fname)

# Conta quantas classes existem (tamanho da lista de nomes únicos das classes)
ncls = len(data['cls-orig'])  # Por exemplo, 3 para o dataset Iris

# Recupera o vetor com a contagem de elementos de cada classe
ncount = data['cls-count']

# Exibe o número total de classes
print(f'1 - possui {ncls} classes')

# Exibe quantos itens há em cada classe
print(f'2 - numero de itens para cada classe: {ncount}')

# Soma total de elementos no conjunto
soma = np.sum(data['cls-count'])

# Calcula o índice de desbalanceamento para cada classe
result = []
for valor in data['cls-count']:
    result.append(soma / valor)  # Soma total dividido pelo número de itens da classe atual

# Encontra o maior valor de IR, ou seja, a maior desproporção entre classes
max = np.max(result)
print('valor max', max)  # Quanto maior esse valor, mais desbalanceado o dataset
