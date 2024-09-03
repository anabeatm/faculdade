# Um professor precisa armazenar em uma lista os nomes dos alunos presentes em um minicurso. 
# Faça um programa para armazenar 5 nomes e permitir que o professor digite o nome de cada um. 
# Em seguida, apresente na tela todos os nomes informados.
nomesAlunos = [""] * 5
for i in range(0, len(nomesAlunos)):
    nomesAlunos[i] = input(f"Digite o nome do {i+1}° aluno: ")
    print(f"A lista dos alunos: {nomesAlunos}")
