# 1 - Criar uma função que recebe por parâmetro um dicionário com os dados de uma nova venda e escreve no final do arquivo.
def novaVenda(listaVendas):
    arquivoLoja = open("loja.csv", "a", encoding="UTF-8")
    
    for i in range(0, len(listaVendas)):
        venda = listaVendas[i]
        linha = venda["nomeCliente"] + "," + venda["dataVenda"] + "," + venda["qntdItensVendidos"] + "," + venda["valorTotal"] + "\n"

        arquivoLoja.write(linha)

    arquivoLoja.close()

# 2 - Criar uma função que recebe por parâmetro o nome de um cliente e retorna um vetor de dicionários de vendas do cliente
# (pesquisar pelo nome ou parte dele).
def vendasCliente(nomeCliente):
    arquivoLoja = open("loja.csv", "r", encoding="UTF-8")
    listaArquivo = arquivoLoja.readlines()

    quantidadeVendas = 0

    for linha in listaArquivo:
        linha = linha.strip()
        dados = linha.split(",")

        if(nomeCliente in dados[0]):
            quantidadeVendas += 1
    
    i_vendas = 0
    vendasCliente = [""] * quantidadeVendas
    
    for i in range(0, len(listaArquivo)):
        linha = listaArquivo[i].strip()
        dados = linha.split(",")

        if(nomeCliente in dados[0]):
            vendasCliente[i_vendas] = {}
            vendasCliente[i_vendas]["nomeCliente"] = dados[0]
            vendasCliente[i_vendas]["dataVenda"] = dados[1]
            vendasCliente[i_vendas]["qntdItensVendidos"] = dados[2]
            vendasCliente[i_vendas]["valorTotal"] = dados[3]
            i_vendas += 1

    arquivoLoja.close()

    return vendasCliente

# 3 - Criar uma função que recebe por parâmetro o nome de um cliente e retorna um dicionário com a quantidade de 
# itens vendidos e o valor total de vendas do cliente (pesquisar pelo nome ou parte dele).
def qntdItensValorTotal(nomeCliente):
    arquivoLoja = open("loja.csv", "r", encoding="UTF-8")
    listaArquivo = arquivoLoja.readlines()

    qntdItensVendidos = 0
    valorTotal = 0

    for linha in listaArquivo:
        linha = linha.strip()
        dados = linha.split(",")

        if(nomeCliente in dados[0]):
            qntdItensVendidos += float(dados[2])
            valorTotal += float(dados[3])

    vendasCliente = {}
    vendasCliente["qntdItensVendidos"] = qntdItensVendidos
    vendasCliente["valorTotal"] = valorTotal

    arquivoLoja.close()

    return vendasCliente


# 4 - Criar uma função que recebe por parâmetro um mês e um ano e retorna um vetor de dicionários com todas as vendas desse período 
# (pesquisar pelo número do mês e ano).
def vendasPorPeriodo(mes, ano):
    arquivoLoja = open("loja.csv", "r", encoding="UTF-8")
    listaArquivo = arquivoLoja.readlines()

    tamanhoDoVetor = 0
    for linha in listaArquivo[1:]:
        linha = linha.strip()
        dados = linha.split(",")
        if(len(dados) > 1):
            data = dados[1]
            dataSplit = data.split("-")
            if(len(dataSplit) == 3):
                mesVenda = dataSplit[1]
                anoVenda = dataSplit[0]
                if(mesVenda == mes and anoVenda == ano):
                    tamanhoDoVetor += 1

    vendasPeriodo = [""] * tamanhoDoVetor

    indice = 0
    for linha in listaArquivo[1:]:
        linha = linha.strip()
        dados = linha.split(",")
        if(len(dados) > 1):
            data = dados[1]
            dataSplit = data.split("-")
            if(len(dataSplit) == 3):
                mesVenda = dataSplit[1]
                anoVenda = dataSplit[0]
                if(mesVenda == mes and anoVenda == ano):
                    vendasPeriodo[indice] = {
                        "nome": dados[0],
                        "data": dados[1],
                        "vendas": dados[2]
                    }
                    indice += 1
    
    arquivoLoja.close()

    return vendasPeriodo

# 5 - Criar uma função que recebe por parâmetro um mês e um ano e retorna um dicionário com a quantidade de itens vendidos 
# e o valor total de vendas desse período (pesquisar pelo número do mês e ano).
def qntdValorTotalPeriodo(mes, ano):
    arquivoLoja = open("loja.csv", "r", encoding="UTF-8")
    listaArquivo = arquivoLoja.readlines()

    qntdItens = 0
    valorTotal = 0

    for linha in listaArquivo[1:]:
        linha = linha.strip()
        dados = linha.split(",")

        if(len(dados) > 1):
            data = dados[1]
            dataSplit = data.split("-")

            if(len(dataSplit) == 3):
                mesVenda = dataSplit[1]
                anoVenda = dataSplit[0]

                if(mesVenda == mes and anoVenda == ano):
                    qntdItens += float(dados[2])
                    valorTotal += float(dados[3])
    
    qntdValorTotal = {}

    qntdValorTotal["qntdItensVendidos"] = qntdItens
    qntdValorTotal["valorTotal"] = valorTotal
    
    arquivoLoja.close()

    return qntdValorTotal

# 6 - Criar um menu principal com as opções acima de modo que os dados obtidos por meio do retorno das funções 
# sejam exibidos adequadamente (for e não print(vetor)) na tela.

def menuOpcoes():
    # vendas = [""] * 100 # garantindo total de espaços, já que não saberei até quanto o usuário gostaria de adicionar vendas
    # indice = 0
    while True:
        print("""--- Menu de Opções:
            1. Adicionar venda
            2. Listar venda de um cliente
            3. Quantidade e venda total de um cliente
            4. Listar vendas de um período
            5. Quantidade e total de vendas de um período
            6. Sair
    """)
        valor = int(input("Opção: "))

        # if(valor == 1):
        #     if(indice >= len(vendas)):
        #         print("Limites de vendas atingido!")
        #         continue

        #     venda = {}
        #     venda["nomeCliente"] = input("Nome: ")
        #     venda["dataVenda"] = input("Data (AAAA-MM-DD): ")
        #     venda["qntdItensVendidos"] = int(input("Quantidade de Itens Vendidos: "))
        #     venda["valorTotal"] = float(input("Valor Total: "))
            
        #     vendas[indice] = venda
        #     indice += 1

        #     novaVenda(vendas)
        # ESTÁ DANDO ERRO

        if(valor == 2):
            nomeCliente = input("Nome do cliente: ")
            print("-" * 30)
            funcao = vendasCliente(nomeCliente)
            for i in range(0, len(funcao)):
                print(f"Nome do cliente: {funcao[i]['nomeCliente']}")
                print(f"Data da venda: {funcao[i]['dataVenda']}")
                print(f"Quantidade de itens vendidos: {funcao[i]['qntdItensVendidos']}")
                print(f"Valor total: {funcao[i]['valorTotal']}")
                print("-" * 30)

        if(valor == 3):
            nomeCliente = input("Nome do cliente: ")
            print("-" * 30)
            funcao = qntdItensValorTotal(nomeCliente)
            print(f"A quantidade de itens vendidos para {nomeCliente}: {funcao['qntdItensVendidos']}")
            print(f"O valor total para {nomeCliente}: R${funcao['valorTotal']:.2f}")

        if(valor == 4):
            mes = input("Mês: ")
            ano = input("Ano: ")
            print("-" * 30)
            funcao = vendasPorPeriodo(mes, ano)
            print(f"No mês {mes} de {ano}, tiveram as seguintes vendas:")
            for i in range(0, len(funcao)):
                print(f"Nome: {funcao[i]['nome']}\nData: {funcao[i]['data']}\nTotal de vendas: {funcao[i]['vendas']}")
                print("-" * 30)

        if(valor == 5):
            mes = input("Mês: ")
            ano = input("Ano: ")
            print("-" * 30)
            funcao = qntdValorTotalPeriodo(mes, ano)
            print(f"Quantidade total no {mes} em {ano}: {funcao['qntdItensVendidos']}")
            print(f"Valor total: R${funcao['valorTotal']:.2f}")
        
        if(valor == 6):
            print("Saindo...")
            break