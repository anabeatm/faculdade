import funcoes as f
# 1
# while True:
#     novaVenda = {}
#     novaVenda["nomeCliente"] = input("Nome: ")
#     novaVenda["dataVenda"] = input("Data (AAAA/MM/DD): ")
#     novaVenda["qntdItensVendidos"] = input("Quantidade de itens vendidos: ")
#     novaVenda["valorTotal"] = input("Valor total: ")

#     f.novaVenda(novaVenda)
#     continuar = input("Deseja inserir mais? [S/N]: ")
#     if(continuar != "S"):
#         break
# 2
# nomeCliente = input("Nome do cliente: ")
# vendas = f.qntdItensValorTotal(nomeCliente)
# for i in range(0, len(vendas)):
#     print(f"A quantidade de itens vendidos para {nomeCliente}: {vendas['qntdItensVendidos']}")
#     print(f"O valor total para {nomeCliente}: R${vendas['valorTotal']:.2f}")
#     print("-" * 15)

# mes = input("Mês: ")
# ano = input("Ano: ")
# funcao = f.vendasPorPeriodo(mes, ano)
# print(f"No mês {mes} de {ano}, tiveram as seguintes vendas:")
# for i in range(0, len(funcao)):
#     print(f"Nome: {funcao[i]['nome']}\nData: {funcao[i]['data']}\nTotal de vendas: {funcao[i]['vendas']}")
#     print("-" * 25)

# funcao = f.qntdValorTotalPeriodo(mes, ano)
# print(f"Quantidade total no {mes} em {ano}: {funcao['qntdItensVendidos']}")
# print(f"Valor total: R${funcao['valorTotal']:.2f}")

f.menuOpcoes()

