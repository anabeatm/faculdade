# Implemente  um  algoritmo  que  contenha  um  procedimento  responsável  por  exibir  o  seguinte 
# menu ao usuário: 
"""MENU DE OPÇÕES: 
1. Somar dois números 
2. Subtrair dois números 
3. Dividir dois números 
4. Multiplicar dois números 5. Sair """
# No  corpo  principal  do  algoritmo,  o  menu  deverá  ser  exibido  e  a  opção  deverá  ser  solicitada  ao  usuário.  O 
# algoritmo deve emitir uma mensagem “opção inválida” caso o usuário informe um valor diferente das opções 
# do menu. Garanta que o algoritmo seja finalizado apenas quando a opção Sair for informada. (OBS: não precisa 
# implementar as ações do menu, apenas o Sair). 

def menuOpcoes():
    print("""MENU DE OPÇÕES: 
1. Somar dois números 
2. Subtrair dois números 
3. Dividir dois números 
4. Multiplicar dois números 
5. Sair 
""")

while True:
    menuOpcoes()
    opcao = int(input("Sua opção: "))
    if(0 < opcao < 5):
        continue
    elif(opcao == 5):
        print("Saindo...")
        break
    else:
        print("Valor inválido!")
        break
