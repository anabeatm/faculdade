# O que é um procedimento? 

# R-> Executa um conjunto de instruções sem ter um retorno de valor.

# Qual é a sintaxe para se criar um procedimento?
def procedimento():
    print("Olá mundo!")

# Seja acao() um procedimento. Durante o algoritmo, como chamar este procedimento para que 
# seu código seja executado? 

# R-> Apenas acao()

# O que são parâmetros? Para que eles servem?

# R-> Valores passados para o procedimento. Servem para quando um procedimento necessitar de algum valor para ser executado.

# Seja acao(a, b, c) um procedimento que recebe três números inteiros como parâmetro. Como 
# chamar este procedimento para que seu código seja executado? 
def acao(a, b, c):
    soma = a + b + c
    print(f"A soma de {a}, {b}, {c} é {soma}.")

acao(2, 3, 4)
