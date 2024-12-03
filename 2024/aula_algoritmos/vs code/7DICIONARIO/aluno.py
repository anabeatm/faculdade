aluno = {
    "nome" : "Ana Beatriz",
    "matricula" : "20241PVAI",
    "dataDeNascimento" : "09/03/2005",
    "email" : "20241pvai@estudantes.ifpr.edu.br",
    "periodo" : "1° ano de Engenharia de Software"
}

print(f"Olá {aluno['nome']}, sua matrícula é {aluno['matricula']}.")

for k in aluno:
    print("Na chave", k, "tem o dado:", aluno[k])

alunos = [""] * 5

alunos[0] = {}
alunos[0]["nome"] = "Rafael"
alunos[0]["RA"] = "48784PVAI"

for i in range(0, len(alunos)):
    alunos[i] = {}
    alunos[i]["nome"] = input("Nome: ")
    alunos[i]["RA"] = input("RA: ")
    