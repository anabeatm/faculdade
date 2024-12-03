import funcoes as f

# novaVenda = [""]
# for i in range(0, len(novaVenda)):
#     novaVenda[i] = {}
#     novaVenda[i]["nomeCliente"] = input("Nome: ")
#     novaVenda[i]["dataVenda"] = input("Data (AAAA/MM/DD): ")
#     novaVenda[i]["qntdItensVendidos"] = input("Quantidade de itens vendidos: ")
#     novaVenda[i]["valorTotal"] = input("Valor total: ")

# f.novaVenda(novaVenda)

# nomeCliente = input("Nome do cliente: ")
# funcao = f.qntdItensValorTotal(nomeCliente)

# print(f"A quantidade de itens vendidos para {nomeCliente}: {funcao['qntdItensVendidos']}")
# print(f"O valor total para {nomeCliente}: R${funcao['valorTotal']:.2f}")

# mes = input("Mês: ")
# ano = input("Ano: ")
# # funcao = f.vendasPorPeriodo(mes, ano)
# # print(f"No mês {mes} de {ano}, tiveram as seguintes vendas:")
# # for i in range(0, len(funcao)):
# #     print(f"Nome: {funcao[i]['nome']}\nData: {funcao[i]['data']}\nTotal de vendas: {funcao[i]['vendas']}")
# #     print("-" * 25)

# funcao = f.qntdValorTotalPeriodo(mes, ano)
# print(f"Quantidade total no {mes} em {ano}: {funcao['qntdItensVendidos']}")
# print(f"Valor total: R${funcao['valorTotal']:.2f}")

f.menuOpcoes()

