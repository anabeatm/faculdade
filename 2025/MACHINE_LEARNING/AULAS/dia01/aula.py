import pandas as pd
# %%
df = pd.read_csv(r"C:\Users\anabe\faculdade\2025\MACHINE_LEARNING\AULAS\dia01\pedrinhas.csv")

print(df)

# %%
colunaClassificacao = df.columns[-1]
classificacao = df[colunaClassificacao]
print(classificacao)

# %%
colunaDesceu = df.columns[1]
desceu = df[colunaDesceu]
print(desceu)

# %%
joao = 0
somaJoao = 0
maria = 0
somaMaria = 0

for i in range(len(classificacao)):
    if(classificacao.iloc[i] == 1): # acesso a posição numérica da linha/coluna
        joao += 1
        somaJoao += desceu.iloc[i]
    elif(classificacao.iloc[i] == 2):
        maria += 1
        somaMaria += desceu.iloc[i]

print("Maria pontuou: ", maria)
print("João pontuou: ", joao)

# %%
mediaJoao = somaJoao / joao if joao > 0 else 0 # evita divisão por 0
print("Média do João: ", mediaJoao)

# %%
mediaMaria = somaMaria / maria if maria > 0 else 0
print("Média da Maria: ", mediaMaria)

