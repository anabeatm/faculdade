"""
Criar dicionário com: nome, matrícula,
data de nascimento, email e período (ano curso)
"""
alunos = [""] * 5

# Criar dicionários "na mão" dentro do vetor
# alunos[0] = {}
# alunos[0]["nome"] = "Rafael Zottesso"
# alunos[0]["ra"] = "123456"

# Criando outro dicionário diferente, porém com os mesmos nomes de chaves
# alunos[1] = {}
# alunos[1]["nome"] = "Fulano de tal"
# alunos[0]["ra"] = "987654"


# Preenchendo um vetor com dicionários #

for i in range(0, len(alunos)):
    # Cria um dicionário dentro da posição "i" do vetor
    alunos[i] = {}
    
    print(f"Preenchendo a posição {i} do vetor")
    
    # Cria a chave "nome" na posição "i" do vetor e guarda uma string
    alunos[i]["nome"] = input("Nome: ")
    # Cria a chave "matricula" na posição "i" do vetor e guarda outra string
    alunos[i]["matricula"] = input("Matrícula: ")
    
    
# Percorrendo um vetor de dicionários #

print("\n\nRelatório de alunos")
# Conta o tamanho do vetor
print("Você tem", len(alunos), "alunos.")
print("Eles são....\n")

# Percorre o vetor
for i in range(0, len(alunos)):
    # Acessa a chave "nome" do dicionário que está na posição "i" do vetor
    print("Nome:", alunos[i]["nome"])
    # Acessa a chave "matricula" do dicionário que está na posição "i" do vetor
    print("RA:", alunos[i]["matricula"])
    # Mostra 20 risquinhos na tela
    print("-" * 20)
    

# C O N T E Ú D O   A D I C I O N A L (não obrigatório)    

# Outra forma de percorrer vetores de dicionários
# Sem se preocupar com as chaves e valores  
print("#" * 20)
print("\n")

# Percorre o vetor
for i in range(0, len(alunos)):
    # Percorre os dicionários dentro do vetor
    for k in alunos[i]:
        print(f"{k.capitalize()}: {alunos[i][k]}")
    print("-" * 20)