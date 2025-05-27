# %%
def conta(lista):
    resultado = {1: 0, 2: 0, 3: 0, 'mar': 0}
    for i in lista:
        if isinstance(i, str) and i.isdigit():
            i = int(i)
        if i not in (1, 2, 3, 'mar'): continue
        resultado[i] += 1
    print("resultado: ", resultado)
    
# %%
conta([1, 2, 3, 2, 1, 2, 3, 1, 2])

# %%
conta([1, 2, 3, 2, '1', 2, 3, 1, 2, 4, 4, 'mar', 'banana', 4, 'mar'])

