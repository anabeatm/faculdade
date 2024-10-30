import random
def retornarNum():
    numero = int(input("Número inteiro: "))

    return numero

def aleatorioNum(numero):
    numAleatorio = random.randint(1, numero)

    return numAleatorio

def aleatorioNumPar(superior, inferior):
    while True:
        numeroAleatorioPar = random.randint(superior, inferior)
        if(numeroAleatorioPar % 2 == 0):
            return numeroAleatorioPar
        
def aleatorioNumImpar(superior, inferior):
    while True:
        numeroAleatorioImpar = random.randint(superior, inferior)
        if(numeroAleatorioImpar % 2 != 0):
            return numeroAleatorioImpar

def numerosMeses(numero):
    if(numero == 1):
        print("Janeiro")
    elif(numero == 2):
        print("Fevereiro")
    elif(numero == 3):
        print("Março")
    elif(numero == 4):
        print("Abril")
    elif(numero == 5):
        print("Maio")
    elif(numero == 6):
        print("Junho")
    elif(numero == 7):
        print("Julho")
    elif(numero == 8):
        print("Agosto")
    elif(numero == 9):
        print("Setembro")
    elif(numero == 10):
        print("Outubro")
    elif(numero == 11):
        print("Novembro")
    elif(numero == 12):
        print("Dezembro")

def quadradoDeX(area):
    aoQuadrado = area ** 2
    return aoQuadrado

def areaRetangulo(base, altura):
    areaRetangulo = base * altura
    return areaRetangulo

def areaTriangulo(base, altura):
    areaTriangulo = (base * altura) / 2
    return areaTriangulo

def areaTrapezio(baseMaior, baseMenor, altura):
    areaTrapezio = ((baseMaior + baseMenor) * altura) / 2
    return areaTrapezio



def menu():
    print("""--- MENU DE OPÇÕES: ---
    1. Retornar número solicitado 
    2. Número aleatório 
    3. Número aleatório par ou ímpar
    4. Números e seus respectivos meses
    5. Calcular a área de um quadrado
    6. Calcular a área do retângulo
    7. Calcular a área do triângulo
    8. Calcular a área do trapézio
    22. Sair
""")
    resultado = int(input("Qual opção deseja: "))
    return resultado
    