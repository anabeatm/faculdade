import pandas as pd

arquivo = pd.read_csv(r'C:\Users\anabe\faculdade\2025\MACHINE_LEARNING\AULAS\dia01\pedrinhas.csv')
#print('ttmp=', arquivo)

print(arquivo.columns)

classificacao = arquivo['classificacao']
pedrinha = arquivo['desceu']
soma = {'joao': 0 , 'maria': 0}
conta = {'joao': 0, 'maria': 0}
for cls, dsc in zip(classificacao, pedrinha):
    if cls == 1: key = 'joao'
    if cls == 2: key = 'maria'
    soma[key] = soma[key] + dsc
    conta[key] += 1

media = {'joao': 0, 'maria': 0}
media['joao'] = soma['joao']/conta['joao'] # type: ignore
media['maria'] = soma['maria']/conta['maria'] # type: ignore
print('media eh:', media)