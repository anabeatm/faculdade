import pandas as pd

lista = [1, 2, 3, 2, '1', 2, 3, 1, 2, 4, 4, 'mar', 'banana', 4, 'mar'] #lista com valores 

df = pd.DataFrame(lista, columns=['Valores']) #usando a função data frame para transformar lista em colunas

contagem = df['Valores'].value_counts() 
print(contagem)