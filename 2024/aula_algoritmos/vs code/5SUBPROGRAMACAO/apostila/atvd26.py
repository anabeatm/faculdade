"""As palavras “ovo”, “Ana”, “Arara”, “mamam”, “ralar”, “rir”, “salas”, “aibofobia” são palíndromos, 
ou seja, são palavras que podem ser lidas do início ao fim ou do fim ao início. Podemos ter frases palíndromos 
(desconsiderando espaços em branco), tais como “o galo ama o lago”, “a base do teto desaba”, “a cara rajada 
da jararaca”, “ato idiota”, “anotaram a data da maratona”, “a gorda ama a droga”, “a grama é amarga”, “a 
sacada  da  casa”.  Implemente  uma  função  chamada  ePalindromo  que  receba  como  parâmetro  uma  String. 
Esta função deverá retornar True caso o parâmetro seja um palíndromo, ou False, caso contrário."""

def ePalindromo(frase):
    frase = frase.replace(" ", "").lower()
    tamanho = len(frase)

    for i in range(tamanho // 2):
        if(frase[i] != frase[tamanho - i - 1]):
            return False
    return True

frase = input("Escreva uma frase: ")
resultado = ePalindromo(frase)
print(resultado)