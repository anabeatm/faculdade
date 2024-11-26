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
        return "Janeiro"
    elif(numero == 2):
        return "Fevereiro"
    elif(numero == 3):
        return "Março"
    elif(numero == 4):
        return "Abril"
    elif(numero == 5):
        return "Maio"
    elif(numero == 6):
        return "Junho"
    elif(numero == 7):
        return "Julho"
    elif(numero == 8):
        return "Agosto"
    elif(numero == 9):
        return "Setembro"
    elif(numero == 10):
        return "Outubro"
    elif(numero == 11):
        return "Novembro"
    elif(numero == 12):
        return "Dezembro"
    else:
        return "Mês inválido"

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

def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def maiorVetor(vetor):
    maiorVetor = vetor[0]
    for i in range(1, len(vetor)):
        if(vetor[i] > vetor[0]):
            maiorVetor = vetor[i]
    return maiorVetor

def menorVetor(vetor):
    menorVetor = vetor[0]
    for i in range(1, len(vetor)):
        if(vetor[i] < vetor[0]):
            menorVetor = vetor[i]
    return menorVetor

def mediaVetor(vetor):
    soma = 0
    for i in range(0, len(vetor)):
        soma += vetor[i]
    mediaArit = soma / len(vetor)
    return mediaArit

def mesPorExtenso(mes):
    if(mes == '01'):
        return "Janeiro"
    elif(mes == '02'):
        return "Fevereiro"
    elif(mes == '03'):
        return "Março"
    elif(mes == '04'):
        return "Abril"
    elif(mes == '05'):
        return "Maio"
    elif(mes == '06'):
        return "Junho"
    elif(mes == '07'):
        return "Julho"
    elif(mes == '08'):
        return "Agosto"
    elif(mes == '09'):
        return "Setembro"
    elif(mes == '10'):
        return "Outubro"
    elif(mes == '11'):
        return "Novembro"
    elif(mes == '12'):
        return "Dezembro"
    else:
        return "Mês inválido"

def formatarData(data):
    data = data.strip()
    dia = data[0:2]
    mes = data[3:5]
    ano = data[6:]
    mesExtenso = mesPorExtenso(mes)
    dataFormatada = dia + " de " + mesExtenso + " de " + ano
    return dataFormatada

def inversoNumero(numero):
    numeroInvertido = numero[::-1]
    numeroInvertido = int(numeroInvertido)
    return numeroInvertido

def inversoNome(nome):
    nomeInvertido = nome[::-1]
    return nomeInvertido

def contarVogais(nome):
    vogais = 'aeiouAEIOU'
    contador = 0
    for caractere in nome:
        if(caractere in vogais):
            contador += 1

    return contador

def embaralharPalavras(texto):
    texto = texto.lower() # a função começa convertendo a string texto para minúsculas, garantindo que o resultado esteja todo em caixa baixa
    tamanho = len(texto) # em seguida, define variáveis auxiliares: tamanho, que guarda o comprimento da string
    textoEmbaralhado = ""  # textoEmbaralhado uma string vazia onde serão armazenados os caracteres embaralhados
    indicesUsados = "" # e indicesUsados, também vazia, que registra os índices já selecionados para evitar repetições

    while(len(textoEmbaralhado) < tamanho): # a função então entra em um loop que continua até textoEmbaralhado ter o mesmo tamanho que a string original
        i = random.randint(0, tamanho - 1) # em cada iteração, ela gera um índice aleatório que aponta para um caractere de texto verificando se esse índice já foi usado
        if(str(i) not in indicesUsados): # se não foi, o caractere correspondente é adicionado a textoEmbaralhado e o índice é registrado em indicesUsados
            textoEmbaralhado += texto[i]
            indicesUsados += str(i)
    # assim, o loop segue até todos os caracteres serem incluídos de forma aleatória em textoEmbaralhado, que é então retornada como a string embaralhada
    return textoEmbaralhado

def gerarSenha(tamanho):
    letrasMaiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letrasMinusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    caracteresEspeciais = "!@#$%&*()-+[{]}?"
    todosCaracteres = letrasMaiusculas + letrasMinusculas + numeros + caracteresEspeciais
    
    senha = ""
    
    for i in range(0, tamanho):
        indiceAleatorio = random.randint(0, len(todosCaracteres) - 1)
        senha += todosCaracteres[indiceAleatorio]
    
    return senha

def percentualAumento(cargo):
    if(cargo == "gerente"):
        return 10
    elif(cargo == "engenheiro"):
        return 20
    elif(cargo == "técnico" or cargo == "tecnico"):
        return 30
    else:
        return 5
def calcularNovoSalario(salario, cargo):
    aumentoPercentual = percentualAumento(cargo)
    aumento = (salario * aumentoPercentual) / 100
    novoSalario = aumento + salario

    return novoSalario

def fatorialRecursivo(numero):
    if(numero == 1 or numero == 0):
        return 1
    else:
        return numero * fatorialRecursivo(numero - 1)


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
    9. Calcular o fatorial de um número 
    10. Maior valor de um vetor
    11. Menor valor de um vetor
    12. A média de um vetor
    13. Data por extenso
    14. O inverso de um número inteiro
    15. O inverso de um nome
    16. Quantas vogais há no nome?
    17. Palavras embaralhadas
    18. Gerar senha
    19. Calcular novo salário
    20. Fatorial Recursivo
""")
    resultado = int(input("Qual opção deseja: "))
    return resultado
    