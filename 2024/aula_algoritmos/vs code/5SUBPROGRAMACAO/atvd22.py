#  Elabore um algoritmo que faça o que se pede:  

# • No programa principal, solicite ao usuário pelo número N de valores a ser informado;  
# • Implemente  um  módulo  que  receba  o  número  N  de  valores  por  parâmetro.  Este  módulo  deve  ser 
# capaz de fazer a leitura de N números e solicitar ao usuário por um número a ser buscado dentro deste 
# conjunto de valores. Por fim, apresente uma mensagem indicado se o valor buscado está presente ou 
# não no conjunto (usando o tópico abaixo);  
# • Implemente um módulo que receba o conjunto de números e o número a ser buscado por parâmetro. 

# O  módulo  deverá  retornar  True  caso  o  valor  buscado  esteja  presente  no  conjunto,  ou  False  caso 
# contrário.

def adicionandoValores(num):
    for i in range(0, len(num)):
        num[i] = float(input(f"Informe o {i + 1}° valor: "))
    return num


def ordenandoValores(num):
    for i in range(0, len(num) - 1):
        iMenor = i
        for j in range(i + 1, len(num)):
            if(num[j] < num[iMenor]):
                iMenor = j
        
        aux = num[i]
        num[i] = num[iMenor]
        num[iMenor] = aux

def buscandoValores(num, valorBuscado):
    comeco = 0
    fim = len(num) - 1

    while(comeco <= fim):
        meio = (comeco + fim) // 2
        if(valorBuscado == num[meio]):
            return True
        else:
            if(valorBuscado > num[meio]):
                comeco = meio + 1
            else:
                fim = meio - 1        
    return False

tamNum = int(input("Quantos números gostaria de armazenar? R: "))
num = [0.0] * tamNum

adicionandoValores(num)
ordenandoValores(num)

valorBuscado = float(input("Informe o valor que deseja buscar: "))


if(buscandoValores(num, valorBuscado)):
    print("O número foi encontrado!")
else:
    print("Número não encontrado!")
