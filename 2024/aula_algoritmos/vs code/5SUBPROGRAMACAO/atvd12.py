# (continuação 11) Implemente os seguintes procedimentos:  
# • somar(): este procedimento deverá solicitar por dois números e apresentar a soma dos dois números 
# informados.  
# • subtrair():  este  procedimento  deverá  solicitar  por  dois  números  e  apresentar  a  subtração  dos  dois  
# números  
# • dividir(a,  b):  este  procedimento  deverá  realizar  a  divisão  do  maior  número  pelo  menor  número 
# informado  nos  parâmetros  e  apresentar  ao  usuário.  Solicitar  dois  números  no  algoritmo  principal e 
# informa-los ao procedimento.  
# • multiplicar(a, b): este procedimento deverá multiplicar os dois valores informados nos parâmetros e 
# apresentar  o  resultado  ao  usuário.  Solicitar  os  dois  valores  no  algoritmo  principal  e  informa-los  ao 
# procedimento. 
 
# Chame os procedimentos correspondentes às ações informadas no menu.
def menuOpcoes():
    print("""MENU DE OPÇÕES: 
1. Somar dois números 
2. Subtrair dois números 
3. Dividir dois números 
4. Multiplicar dois números 
5. Sair 
""")

def somar():
    a = float(input("O primeiro valor: "))
    b = float(input("O primeiro valor: "))
    resultado = a + b
    print(f"Resultado: {resultado}")

def subtrair():
    a = float(input("O primeiro valor: "))
    b = float(input("O primeiro valor: "))
    if(a > b):
        resultado = a - b
    else:
        resultado = b - a
    print(f"Resultado: {resultado}")

def dividir(a, b):
    if(a > b):
        resultado = a / b
    else:
        resultado = b / a
    print(f"Resultado: {resultado}")

def multiplicar(a, b):
    resultado = a * b
    print(f"Resultado: {resultado}")

while True:
    menuOpcoes()
    opcao = int(input("Sua opção: "))
    if(opcao == 1):
        somar()
    elif(opcao == 2):
        subtrair()
    elif(opcao == 3):
        a = float(input("O primeiro valor: "))
        b = float(input("O primeiro valor: "))
        dividir(a, b)
    elif(opcao == 4):
        a = float(input("O primeiro valor: "))
        b = float(input("O primeiro valor: "))
        multiplicar(a, b)
    if(0 < opcao < 5):
        continue
    elif(opcao == 5):
        print("Saindo...")
        break
    else:
        print("Valor inválido!")
        break
