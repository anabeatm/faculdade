# Importa as bibliotecas pandas e numpy
import pandas as pd
import numpy as np

# Define uma função que carrega e processa um conjunto de dados a partir de um arquivo CSV
def data_set(fname):
    result = {}  # Dicionário para armazenar os resultados
    result['nome-arquivo'] = fname  # Salva o nome do arquivo no dicionário

    # Lê o arquivo CSV usando pandas
    data = pd.read_csv(fname)

    # Obtém a lista de colunas do DataFrame
    cols = data.columns

    # Pega o nome da última coluna, que normalmente contém as classes (rótulos)
    ultima = cols[-1]

    # Armazena a coluna de classes originais
    nome_orig = data[ultima]

    # Usa numpy para:
    # - cls_orig: lista de nomes das classes únicas
    # - classes: rótulos numéricos associados a cada item (inteiros, como 0, 1, 2)
    # - cls_count: contagem de elementos de cada classe
    cls_orig, classes, cls_count = np.unique(nome_orig, return_inverse=True, return_counts=True)

    # Remove a coluna de classes do DataFrame original, ficando apenas com os dados (features)
    df = data.drop(columns=ultima)

    # Armazena os dados e informações processadas no dicionário de resultados
    result['dados'] = df                  # Apenas as características (sem os rótulos)
    result['classes'] = classes           # Rótulos numéricos convertidos (por exemplo, [0, 1, 2, ...])
    result['cls-orig'] = cls_orig         # Nomes reais das classes (por exemplo, ['Iris-setosa', ...])
    result['cls-count'] = cls_count       # Quantidade de instâncias por classe

    return result  # Retorna o dicionário com todas as informações

# Caminho do arquivo CSV com os dados (exemplo: base de dados Iris)
fname = r'C:\Users\anabe\faculdade\2025\MACHINE_LEARNING\AULAS\dia04\iris_dataSet.csv'

# Verifica se este script está sendo executado diretamente (e não importado como módulo)
if __name__ == '__main__':
    # Executa a função de carregamento e processamento
    data = data_set(fname)

    # Imprime cada chave e valor do dicionário de resultados
    for key, value in data.items():
        print(f'{key} ---> {value}')
