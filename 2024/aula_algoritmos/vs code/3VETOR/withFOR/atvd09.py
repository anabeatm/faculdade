# Um professor precisa armazenar uma lista de n alunos e seus respectivos conceitos. 
# Crie um programa para auxiliar este professor.
numerosAlunos = int(input("Informe quantos alunos há na turma: "))

nomeAlunos = [""] * numerosAlunos

for i in range(0, len(nomeAlunos)):
    nomeAlunos[i] = input(f"Informe o nome do {i + 1}° aluno(a): ")

print(nomeAlunos)
