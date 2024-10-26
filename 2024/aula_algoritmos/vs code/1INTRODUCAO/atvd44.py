# Uma loja está com uma promoção em compras acima de R$500. Acima desse valor, a loja
#  oferece 10% de desconto se o cliente pagar por PIX ou 5% de desconto para outras
#  formas de pagamento. Por outro lado, para compras abaixo de R$500, a loja oferece
#  apenas 5% de desconto se o pagamento for por PIX. Faça um programa que receba um
#  valor e a forma de pagamento, calcule e imprima o valor do desconto e o valor final da
#  compra

valor = float(input("Qual o valor total da compra? R$"))

if(valor > 500):
    pagamento_cartao_pix = input("Qual será o método de pagamento [PIX/cartão]: ").upper()
    if(pagamento_cartao_pix == "PIX"):
        desconto = valor - (10 / 100)
        print(f"O valor total de {valor} ficará R${desconto}.")
    if(pagamento_cartao_pix == "CARTÃO"):
        desconto = valor - (5 / 100)
        print(f"O valor total de {valor} ficará R${desconto}.")

if(valor < 500):
    pagamento_cartao_pix = input("Qual será o método de pagamento [PIX/cartão]: ").upper()
    if(pagamento_cartao_pix == "PIX"):
        desconto = valor - (5 / 100)
        print(f"O valor total de {valor} ficará R${desconto}.")
    if(pagamento_cartao_pix == "CARTÃO"):
        print(f"O valor total é R${valor}.")

