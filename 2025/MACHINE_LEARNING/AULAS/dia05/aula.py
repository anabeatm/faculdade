import pandas as pd
import numpy as np

def dataSet(fname):
    result = {}
    result['nomeArquivo'] = fname

    data = pd.read_csv(fname)
    cols = data.columns
    ultima = cols[-1]

    nomeOriginal = data[ultima]
    clsOriginal, classes = np.unique(nomeOriginal, return_inverse=True)
    
    print(classes)
    print(clsOriginal)
    
    df = df.drop(columns=ultima)


    result['dados'] = df



    print(data[ultima])

    return result

FNAME = r'caminho do arquivo!!'

if __name__ == '__main__': # serve para executar um bloco de código apenas quando o arquivo é executado diretamente, 
# e não quando ele é importado como módulo em outro arquivo
    data = dataSet(FNAME)
    print(data)
    print(data)
