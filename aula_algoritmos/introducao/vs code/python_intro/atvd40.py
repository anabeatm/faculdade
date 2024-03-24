# Faça um programa que peça para o usuário digitar um número inteiro. Se esse número for
#  negativo, peça para ele digitar um número novamente. Por fim, independente do valor,
#  multiplique o número por 10 e informe o resultado na tela.
num = int(input("Digite um numero inteiro: "))

if(num < 0):
    num = int(input("Digite um numero inteiro novamente: "))
    vezesDez = num * 10
    print(vezesDez)
else:
    print("Fim do programa :)")
    