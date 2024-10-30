# As variáveis declaradas nos parâmetros de um procedimento, assim como as variáveis declaradas 
# dentro do procedimento, são variáveis chamadas de Locais ou Globais? Por que?

# R -> Locais, pois só a variável só existe dentro do procedimento em que foi criada, fora dele não há efeito.

# Qual é a diferença entre variáveis locais de variáveis globais?

# R -> Variáveis locais só tem efeito dentro do módulo onde foi criada. Já globais podem afetar tanto o procedimento em que foi chamada, quanto no resto do código.

# Seja idade = 20 uma variável definida no algoritmo. Como fazer para que esta variável possa ser 
# modificada dentro de um procedimento? 

idade = 20

def exibirIdade():
    global idade
    idade = 19
    print(f"Sua idade é {idade} anos.")

exibirIdade()

# Implemente um procedimento que seja capaz de exibir a mensagem “Olá Pessoal”. Chame este 
# procedimento 4x. 

def exibirMensagem():
    print("Olá Pessoal!")

exibirMensagem()

exibirMensagem()

exibirMensagem()

exibirMensagem()

# Implemente um procedimento que seja capaz de solicitar por um número e apresentar se este 
# número é par ou ímpar. Chame este procedimento 5x.

def parOuImpar(num):
    if((num % 2) == 0):
        print("O número é par!")
    else:
        print("O número é ímpar!")

parOuImpar(num = int(input("Informa um número: ")))

