#%%
import pandas as pd
import numpy as np


wine_DataSet = r'C:\Users\anabe\faculdade\2025\MACHINE_LEARNING\EXERCICIOS\pra_prova\01\wine.csv'

# - Contar quantas classes existem no conjunto de dados
# - Contar quantos registros existem por classe
# - Calcular o desbalanceamento das classes (Índice de Desbalanceamento - IR)

def data_set(fileName):
    dataSet_dic = {}
    
    dataSet_dic['file-name'] = fileName

    # ler data set
    data = pd.read_csv(fileName)

    # obter todas as colunas do data set 
    colunas = data.columns

    # obter as  labels do data set
    labels = colunas[0]

    # armazenar as labels originais em outra variável
    labels_originais = data[labels]

    # usar o numpy para obter as labels individuais e a qntd delas
    labels_indiv, labels_qntd = np.unique(labels_originais, return_counts=True)

    # dropar a coluna das labels
    df = data.drop(columns=labels)

    # colocar cada dado no dicionario
    dataSet_dic['features'] = df
    dataSet_dic['labels'] = labels_originais
    dataSet_dic['labels-unicas'] = labels_indiv
    dataSet_dic['labels-count'] = labels_qntd

    # return dicionario
    return dataSet_dic
#%%
dataSet = data_set(wine_DataSet)

#%%
# 01
qntdLabels = len(dataSet['labels-unicas'])
print(qntdLabels)

# %%
# 02
qntdRegistro = dataSet['labels-count']
print(qntdRegistro)

#%%
# 03
soma = np.sum(qntdRegistro)
irResult = []
for valor in qntdRegistro:
    irResult.append(soma / valor)

print(irResult)
max = np.max(irResult)
print('valor max', max)

min = np.min(irResult)
print('valor min', min)

# %%
