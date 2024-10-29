# Elabore  uma  função  que  receba  4  números  inteiros  nos  parâmetros  e  retorne  o  maior  dos 
# números.  
def maiorNum(num1, num2, num3, num4):
    maior = num1
    if(num2 > maior):
        maior = num2
    if(num3 > maior):
        maior = num3
    if(num4 > maior):
        maior = num4
    return maior


num1 = int(input(f"Informa o 1° valor: "))
num2 = int(input(f"Informa o 2° valor: "))
num3 = int(input(f"Informa o 3° valor: "))
num4 = int(input(f"Informa o 4° valor: "))

print("O maior número é:", maiorNum(num1, num2, num3, num4))
