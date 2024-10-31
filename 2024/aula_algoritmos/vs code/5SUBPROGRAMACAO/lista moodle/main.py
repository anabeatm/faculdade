# Faça um programa principal com menu para exibir as opções e executar as funções criadas nesta lista de exercícios.
import funcoes

# Crie uma função para pedir um número inteiro ao usuário e retornar ele. 
# Toda vez que você precisar de um número informado pelo usuário, utilize ela. 
# Ela não tem parâmetro e o retorno é o valor digitado pelo usuário já com o tipo inteiro.

# Construa um programa com menu e cada exercício abaixo deve ser uma opção dele. A opção pode ser o número do exercício.

opcao = funcoes.menu()


# Faça uma função para gerar números aleatórios. Esta função deve receber um número inteiro por parâmetro e 
# retornar um número aleatório entre 1 e ele. Assim, toda vez que você precisar de um número qualquer pode usar 
# a função do exercício 1 ou esta.

# Crie duas funções para sortear números aleatórios. As funções devem receber o limite inferior e o superior por 
# parâmetros. Uma função deve retornar um número par e a outra um número ímpar. Detalhe: uma função não pode ser 
# criada dentro de outra.

# Faça uma função que receba um número inteiro por parâmetro e retorne o mês correspondente ao número. 
# Por exemplo, 2 corresponde a "Fevereiro". Se o número informado não corresponder a um mês (1 a 12), retorne 
# a mensagem “Mês inválido”.

# Faça funções para resolver as equações de área:
# do quadrado = x²  
# do retângulo = b . h 	(base x altura)
# do triângulo= (b . h) / 2
# do trapézio = ((B + b).h) / 2

# Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que n! depende de (n-1)!; 
# este por sua vez depende de (n-2)!; e, assim por diante, até que n seja 1, quando então tem-se que fatorial de 1 é 
# igual a 1 mesmo. Utilize uma função que recebe como parâmetro o número a ser calculado o fatorial, do tipo inteiro, 
# e retorna o fatorial deste número, também do tipo inteiro.

# Faça uma função que receba um vetor como parâmetro e retorne apenas o maior valor deste vetor.

# Faça uma função que receba um vetor como parâmetro e retorne apenas o menor valor deste vetor.

# Faça uma função para receber um vetor como parâmetro, calcular a soma desse vetor e retornar apenas a média dos valores.

# Construa uma função que receba por parâmetro uma data no formato DD/MM/AAAA e devolva uma string no formato DD de Mês 
# Por Extenso de AAAA. Para pegar o mês por extenso, utilize a função criada no exercício 3. Por exemplo: 18/09/2019 
# retorna 18 de Setembro de 2019.

# Faça uma função que retorne o reverso de um número inteiro informado por parâmetro. Por exemplo: 127 retorna 721.



if(opcao == 1):
    resultado = funcoes.retornarNum()
    print("O número solicitado foi:", resultado)

elif(opcao == 2):
    numero = int(input("Número inteiro: "))
    resultado = funcoes.aleatorioNum(numero)
    print("O número aleatório é", resultado)

elif(opcao == 3):
    superior = int(input("Defina o máximo: "))
    inferior = int(input("Defina o mínimo: "))
    resultado = funcoes.aleatorioNumPar(superior, inferior)
    resultadoI = funcoes.aleatorioNumImpar(superior, inferior)
    print("O número aleatório PAR é:", resultado)
    print("O número aleatório ÍMPAR é:", resultadoI)

elif(opcao == 4):
    numero = int(input("Número inteiro entre 1 a 12: "))
    resultado = funcoes.numerosMeses(numero)

elif(opcao == 5):
    area = float(input("Qual o tamanho da área a ser calculada? R: "))
    resultado = funcoes.quadradoDeX(area)
    print(f"A área {area} é: {resultado:.2f}")

elif(opcao == 6):
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    resultado = funcoes.areaRetangulo(base, altura)
    print(f"A área do retângulo é: {resultado:.2f}")

elif(opcao == 7):
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    resultado = funcoes.areaTriangulo(base, altura)
    print(f"A área do triângulo é: {resultado:.2f}")

elif(opcao == 8):
    baseMaior = float(input("Base maior: "))
    baseMenor = float(input("Base menor: "))
    altura = float(input("Altura: "))
    resultado = funcoes.areaTrapezio(baseMaior, baseMenor, altura)
    print(f"A área do trapézio é: {resultado:.2f}")

elif(opcao == 9):
    numero = int(input("Fatorial de: "))
    resultado = funcoes.fatorial(numero)
    print(f"O fatorial de {numero}! é {resultado}.")

elif(opcao == 10):
    tamVetor = int(input("Defina o tamanho do vetor: "))
    vetor = [0] * tamVetor
    for i in range(0, len(vetor)):
        vetor[i] = int(input(f"Coloque o {i + 1}° valor: "))
    resultado = funcoes.maiorVetor(vetor)
    print(f"O maior valor do vetor é {resultado}.")

elif(opcao == 11):
    tamVetor = int(input("Defina o tamanho do vetor: "))
    vetor = [0] * tamVetor
    for i in range(0, len(vetor)):
        vetor[i] = int(input(f"Coloque o {i + 1}° valor: "))
    resultado = funcoes.menorVetor(vetor)
    print(f"O menor valor do vetor é {resultado}.")

elif(opcao == 12):
    tamVetor = int(input("Defina o tamanho do vetor: "))
    vetor = [0] * tamVetor
    for i in range(0, len(vetor)):
        vetor[i] = int(input(f"Coloque o {i + 1}° valor: "))
    resultado = funcoes.mediaVetor(vetor)
    print(f"A média do vetor é {resultado:.2f}")

elif(opcao == 13):
    data = input("Escreva uma data no formato DD/MM/AAAA: ")
    resultado = funcoes.formatarData(data)
    print(resultado)

elif(opcao == 14):
    numero = input("Digite uma sequência númerica: ")
    resultado = funcoes.inversoNumero(numero)
    print(resultado)