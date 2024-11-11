# Crie um procedimento que receba como parâmetro o número total de alunos de uma turma, a 
# quantia de notas obtidas em uma disciplina e o nome da disciplina. O procedimento deverá solicitar o total de 
# notas,  por  aluno e  calcular  a  sua  média  aritmética. Crie  também  um  segundo  procedimento  que  receba os 
# dados informados e o nome da disciplina, sendo que este procedimento deverá apresentar ao usuário uma 
# tabela contendo as três notas e a média, para a disciplina informada.

def turma(totalAlunos, totalNotas, disciplina):
    notas = [0.0] * totalNotas
    alunos = [0] * totalAlunos
    
    for c in range(0, len(alunos)):
        soma = 0
        alunos[c] = input(f"Nome do {c + 1}° aluno: ")
        for i in range(0, len(notas)):
            notas[i] = float(input(f"{i + 1}° nota: "))
            
        for media in range(0, len(notas)):
            soma += notas[media]
            print(soma)
        mediaArit = soma / totalNotas
        print(f"A média do(a) {alunos[c]} é {mediaArit} na disciplina: {disciplina}")           
    
totalNotas = int(input("Qual o total de notas: "))
totalAlunos = int(input("Quantidade de alunos: "))
disciplina = input("Nome da disciplina: ")

turma(totalAlunos, totalNotas, disciplina)
