"""Faça um programa que mostre o menu a seguir, receba a opção do usuário e os dados necessários 
para executar cada operação. O programa será executado repetidamente até que o usuário passe o 
número informado para sair do programa (opção).
====== Menu Principal ======
1. Fazer a tabuada do 1 ao 10 para um número X
2. Apresentar os múltiplos de X entre 1 e 100
3. Apresentar a soma dos números de 1 a X
4. Sair do programa
"""

while True:
    print("""====== Menu Principal ======
1. Fazer a tabuada do 1 ao 10 para um número X
2. Apresentar os múltiplos de X entre 1 e 100
3. Apresentar a soma dos números de 1 a X
4. Sair do programa
""")
    opcaoUsu = int(input("Sua opção: "))
    if(opcaoUsu == 1):
        x = int(input("Informe o valor de x: "))
        tabuada = 0
        for c in range(1, 11):
            tabuada = x * c
            print(f"{c} x {x} = {tabuada}")
    elif(opcaoUsu == 2):
        x = int(input("Informe o valor de x: "))
        multiplos = 0
        for c in range(1, 101):
           if c % x == 0: # exemplo: c = 5 e x = 2, 5 % 2 = 1 -> Falso, não aparecerá no terminal
               print(c)
    elif(opcaoUsu == 3):
        x = int(input("Informe o valor de x: "))
        for c in range(0, x):
            print(c)
    elif(opcaoUsu == 4):
        saida = input("Deseja sair do programa? [s/n]: ").lower()
        if(saida == 's'):
            print("Saindo...")
        break