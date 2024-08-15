#  Uma loja está com uma promoção de 10% desconto em compras acima de R$100. Faça
#  um programa que receba um valor, calcule e imprima o valor do desconto, se existir, e o
#  valor final da compra.
produto = float(input("Qual é o valor do produto: R$"))

if(produto >= 100.00):
    desconto = produto - (produto * (10 / 100))
    print(f"O valor do seu produto é de R${produto} e com esse valor, terá um desconto de 10%.")
    print(f"Seu total ficou R${desconto}.")
else:
    print(f"Seu total ficou R${produto}.")
