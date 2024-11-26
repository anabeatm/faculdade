# arq = open("aula1911.txt", "r", encoding="UTF-8")

# # conteudo = arq.readline()

# # print(conteudo)

# # conteudo = arq.readline()

# # print(conteudo)

# conteudoNoArq = arq.readlines()

# arq.close()

# # print(conteudoNoArq)

# for i in range(0, len(conteudoNoArq)):
#     linha = conteudoNoArq[i].replace("\n", "")
#     dados = linha.split(",")
#     # print(linha)
#     # print(f"Olá {dados[0]}, você tem {dados[1]} anos.")
#     intDados = int(dados[1])

#     if(intDados > 30):
#         print(dados[0])

arq = open("aula1911.txt", "a", encoding="UTF-8")

nome = input("Nome do amigo: ")
idade = int(input("Idade do amigo: "))

linha = f"{nome}, {idade}\n"

arq.write(linha)
arq.close()