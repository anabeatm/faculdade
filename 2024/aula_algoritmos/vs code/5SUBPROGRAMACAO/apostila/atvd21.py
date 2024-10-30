#  Elabore uma função que receba um valor numérico nos parâmetros e retorne True caso o valor 
# seja  positivo  e  False  caso  seja  negativo.  Efetue  testes  diretamente  no  algoritmo  principal  chamando  esta 
# função dentro do comando if. 
def ehPositivo(num):
    return num > 0

num = float(input("Informe um número: "))

if(ehPositivo(num)):
    print("O número é positivo.")
else:
    print("O número é negativo.")