"""O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma tabela que contém 
o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do 
caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. 
Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá 
os preços de 1 até 50 produtos, conforme o exemplo abaixo:

Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50

"""
precoUni = 1.99 # Definindo preço unitário, já que `1 - R$ 1.99`

for c in range(1, 51):
    precoTotal = precoUni * c # Preço total sendo calculado dentro do loop.
    # Para cada `c`, multiplica com `precoUni` nos dando o preço total dos itens.
    print(f"{c} - R${precoTotal:.2f}")