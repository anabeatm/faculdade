def conta (lista):
    result = [0, 0, 0]
    for id in lista:
#        print(id) # teste
        idx = id - 1
        result[idx] += result[idx] + 1
    print(result)

conta([1, 2, 3, 2, 2, 3, 1, 2])

def contaDict(lista):
    result = {1:0, 2:0, 3:0}
    for item in lista:
        if item not in (1, 2, 3): continue # 
        result[item] += 1
    print(result)
contaDict([1, 2, 3, 2, '1', 2, 3, 1, 2, 4, 4, 'mar', 'banana', 4, 'mar'])

# ----------------------------------------------------------------
