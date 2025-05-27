# %%
import pandas as pd
df = pd.read_json(r'C:\Users\anabe\faculdade\2025\MACHINE_LEARNING\AULAS\dia02\pessoas.json')
print(df)

#%%
def contandoNomes(df):
    result = {}
    for nome in df['nomes-pessoas']:
        if(nome in result):
            result[nome] += 1
        else:
            result[nome] = 1
    return result

#%%
print(contandoNomes(df))
# %%
