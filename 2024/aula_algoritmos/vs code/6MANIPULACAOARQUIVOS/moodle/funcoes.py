# 1 - Criar uma função para adicionar uma linha com os dados necessários no arquivo.

def adicionarDados(nome, dataVenda, qntdItensVendidos, valorTotal):
    arquivoLoja = open("loja.csv", "a", encoding="UTF-8")

    linhaLoja = f"{nome},{dataVenda},{qntdItensVendidos},{valorTotal}\n"

    arquivoLoja.write(linhaLoja)

    arquivoLoja.close()

# 2 - Criar uma função para listar todas as vendas de um cliente (pesquisar pelo nome ou parte dele).
def listarVendasCliente(nome):
    arquivoLoja = open("loja.csv", "r", encoding="UTF-8")
    listaArquivo = arquivoLoja.readlines()

    for i in range(0, len(listaArquivo)):
        linha = listaArquivo[i].replace("\n", "")
        dados = linha.split(",")

        if(nome in dados[0]):
            return dados

# 3 - Criar uma função para informar na tela a quantidade e o total de vendas de um cliente (pesquisar pelo nome ou parte dele).
def qntdETotalVendas(nome):
    arquivoLoja = open("loja.csv", "r", encoding="UTF-8")
    listaArquivo = arquivoLoja.readlines()

    quantidadeTotal = 0
    totalVendas = 0

    for linha in listaArquivo:
        linha = linha.strip()
        dados = linha.split(",")
    
        if(nome in dados[0]):
            quantidadeTotal += 1
            totalVendas += float(dados[3])

    arquivoLoja.close()

    respostaFormatada = (
    f"Dados do cliente {nome}:\n"
    f"Quantidade total das vendas: {quantidadeTotal}\n"
    f"Total das vendas: {totalVendas:.2f}")
    
    return respostaFormatada

# 4 - Criar uma função para listar todas as vendas de um mês específico (pesquisar pelo número do mês).
def vendasMes(mes):
    arquivoLoja = open("loja.csv", "r", encoding="UTF-8")
    listaArquivo = arquivoLoja.readlines()


    for i in range(0, len(listaArquivo)):
        linha = listaArquivo[i].split("-")
        for c in range(0, len(linha)):
            if(mes == linha[c]):
                print(f"{linha[c - 1]} - {linha[c]} - {linha[c + 1]}")
    
    arquivoLoja.close()
    
# 5 - Criar uma função para informar a quantidade e o valor total de vendas de um mês específico (pesquisar pelo número do mês).
def qntdEvalorTotalMes(mes):
    arquivoLoja = open("loja.csv", "r", encoding="UTF-8")
    listaArquivo = arquivoLoja.readlines()

    quantidadeTotal = 0
    totalVendas = 0

    for linha in listaArquivo[1:]:
        linha = linha.strip()
        dados = linha.split(",")

        data = dados[1]
        mesVenda = data.split("-")[1]

        if(mes == mesVenda):
            quantidadeTotal += int(dados[2])
            totalVendas += float(dados[3])

    arquivoLoja.close()

    retorno = (f"Quantidade total de vendas do mês {mes}: {quantidadeTotal}\nValor total das vendas do mês {mes}: {totalVendas:.2f}")
    
    return retorno

# 6 - Criar um menu principal com as opções acima
def menuOpcoes():
    while True:
        print("""--- Menu de Opções:
            1. Adicionar venda
            2. Listar venda de um cliente
            3. Quantidade e venda total de um cliente
            4. Listar vendas de um mês
            5. Quantidade e total de vendas de um mês
            6. Sair
    """)
        
        valor = int(input("Opção: "))

        if(valor == 1):
            nome = input("Nome: ")
            dataVenda = input("Data da venda: ")
            qntdItensVendidos = input("Quantidade de itens vendidos: ")
            valorTotal = input("Valor total da venda: ")
            funcao = adicionarDados(nome, dataVenda, qntdItensVendidos, valorTotal)

        elif(valor == 2):
            procuraNome = input("Nome que procura: ")
            funcao = listarVendasCliente(procuraNome)
            print(funcao)

        elif(valor == 3):
            procuraNome = input("Nome que procura: ")
            funcao = qntdETotalVendas(procuraNome)
            print(funcao)

        elif(valor == 4):
            procuraMes = input("Quantidade de vendas do mês: ")
            funcao = vendasMes(procuraMes)

        elif(valor == 5):
            procuraMes = input("Quantidade de vendas do mês: ")
            funcao = qntdEvalorTotalMes(procuraMes)
            print(funcao)

        elif(valor == 6):
            print("Saindo ...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 6.")