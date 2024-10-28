# Um esquema de sorteio precisa armazenar um banco de 10 palavras informadas pelo usuário e ao final 
# sortear uma delas aleatoriamente. Em seguida, o programa deve perguntar para o usuário uma letra e 
# verificar quantas vezes essa letra aparece na palavra sorteada
from random import choice

palavras = [""] * 10
for i in range(0, len(palavras)):
    palavras[i] = input("Informe uma palavra: ")

palavraSorteada = choice(palavras)
print(f"A palavra sorteada foi {palavraSorteada}!")

letra = input("Qual letra gostaria de verificar? R: ")
cont = 0
for c in range(len(palavraSorteada)):
    if(palavraSorteada[c] == letra):
        cont += 1

print(f"A letra escolhida '{letra}' aparece {cont} vezes.")
