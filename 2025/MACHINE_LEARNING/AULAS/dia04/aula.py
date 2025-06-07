import numpy as np
# Contar quantas classes possui.
# ↳ Contar quantos registros cada classe.
# ↳ Calcular o desbalanceamento.

# IR = ( contagem_classe / total )

from anotProf import data_set

fname = r'C:\Users\anabe\faculdade\2025\MACHINE_LEARNING\AULAS\dia04\iris_dataSet.csv'

data = data_set(fname)
ncls = len(data['cls-orig'])
ncount = data['cls-count']
print(f'1 - possui {ncls} classes')

print(f'2 - numero de itens para cada classe: {ncount}')

soma = np.sum(data['cls-count'])
result = []
for valor in data['cls-count']:
    result.append(soma / valor)

max = np.max(result)
print('valor max', max)
