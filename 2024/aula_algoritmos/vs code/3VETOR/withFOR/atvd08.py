# Roberto é um vendedor que precisa calcular sua comissão mensal. 
# Ele recebe uma porcentagem de cada venda realizada. Crie um algoritmo que solicite ao 
# vendedor o número de vendas efetuadas no mês e armazene-o em uma variável. Utilize um 
# laço de repetição para solicitar o valor de cada venda e armazená-lo em um vetor. 
# Em seguida, calcule a comissão total do vendedor, sabendo que a comissão é:
# 5% para vendas até R$999,99
# 4% para vendas entre R$1.000 e R$1.999
# 3% para vendas acima de R$2.000
vendasMes = int(input("Qual foi o total de vendas no mês? "))
vendas = [0] * vendasMes


comissaoTotal = 0
for i in range(0, len(vendas)):
    venda = float(input(f"Coloque o valor total da {i+1}° venda do mês: "))
    vendas[i] = venda

    if(venda <= 999.99):
        comissao = venda * 0.05

    elif(1000 <= venda <= 1999.99):
        comissao = venda * 0.04

    else:
        comissao = venda * 0.03

    
    comissaoTotal += comissao

print(f"A comissão total é de R${comissaoTotal:.2f}")