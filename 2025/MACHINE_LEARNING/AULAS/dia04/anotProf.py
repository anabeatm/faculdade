import pandas as pd
import numpy as np

def data_set( fname ):
    result = {}
    result['nome-arquivo'] = fname
    data = pd.read_csv(fname)
    cols = data.columns
    ultima = cols[-1]

    nome_orig = data[ultima]
    cls_orig, classes, cls_count = np.unique(nome_orig, return_inverse=True, return_counts=True)

    df = data.drop( columns=ultima )

    result['dados'] = df
    result['classes'] = classes
    result['cls-orig'] = cls_orig
    result['cls-count'] = cls_count

    return result


fname = r'C:\Users\anabe\faculdade\2025\MACHINE_LEARNING\AULAS\dia04\iris_dataSet.csv'
if __name__ == '__main__':
    data = data_set(fname)
    for key, value in data.items():
        print(f'{key} ---> {value}')
