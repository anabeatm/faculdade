def conta_lista(lista):
    result = [0, 0, 0]
    for id in lista:
        if id not in (1,2,3): continue
        idx = id-1
        result[idx] = result[idx]+1
    print('resultado ==>',result)

def conta_dict(lista):
    result = {1: 0, 2: 0, 3: 0}
    for item in lista:
        if item not in (1,2,3): continue
        result[item] = result[item] + 1
    print('resultado ==>', result)


#conta_lista([1, 2, 3, 2, 1, 2, 3, 1, 2])
#conta_dict([1, 2, 3, 2, 1, 2, 3, 1, 2])

conta_lista([1, 2, 3, 2, '1', 2, 3, 1, 2, 4, 4, 'mar', 'banana', 4, 'mar'])
#conta_dict([1, 2, 3, 2, '1', 2, 3, 1, 2, 4, 4, 'mar', 'banana', 4, 'mar'])
