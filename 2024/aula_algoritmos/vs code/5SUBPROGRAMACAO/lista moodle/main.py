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

if(opcao == 1):
    opcao1 = funcoes.retornarNum()
    print("O número solicitado foi:", opcao1)

elif(opcao == 2):
    numero = int(input("Número inteiro: "))
    opcao2 = funcoes.aleatorioNum(numero)
    print("O número aleatório é", opcao2)

elif(opcao == 3):
    superior = int(input("Defina o máximo: "))
    inferior = int(input("Defina o mínimo: "))
    opcao3 = funcoes.aleatorioNumPar(superior, inferior)
    opcao3a = funcoes.aleatorioNumImpar(superior, inferior)
    print("O número aleatório PAR é:", opcao3)
    print("O número aleatório ÍMPAR é:", opcao3a)

elif(opcao == 4):
    numero = int(input("Número inteiro entre 1 a 12: "))
    opcao4 = funcoes.numerosMeses(numero)

elif(opcao == 5):
    area = float(input("Qual o tamanho da área a ser calculada? R: "))
    opcao5 = funcoes.quadradoDeX(area)
    print(f"A área {area} é: {opcao5:.2f}")

elif(opcao == 6):
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    opcao6 = funcoes.areaRetangulo(base, altura)
    print(f"A área do retângulo é: {opcao6:.2f}")

elif(opcao == 7):
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    opcao7 = funcoes.areaTriangulo(base, altura)
    print(f"A área do triângulo é: {opcao7:.2f}")

elif(opcao == 8):
    baseMaior = float(input("Base maior: "))
    baseMenor = float(input("Base menor: "))
    altura = float(input("Altura: "))
    opcao8 = funcoes.areaTrapezio(baseMaior, baseMenor, altura)
    print(f"A área do trapézio é: {opcao8:.2f}")