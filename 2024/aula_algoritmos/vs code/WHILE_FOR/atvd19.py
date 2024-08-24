"""Desenvolva um programa que calcule o custo total de uma viagem com base na distância a ser 
percorrida e o tipo de veículo. O custo por quilômetro varia conforme o tipo de veículo, 
conforme a tabela abaixo:

Tipo de Veículo -------------- Custo por Quilômetro
Econômico  ----------------------  R$ 1,50
Médio ---------------------------- R$ 2,25
Luxo ----------------------------- R$ 3,00

O programa deve solicitar a distância a ser percorrida e o tipo de veículo. Em seguida, 
deve calcular e exibir o custo total da viagem. O programa deve permitir que o usuário faça 
novos cálculos até que ele escolha encerrar.
"""
while True:
    veiculo = input("Informe o tipo de veículo utilizado [E/M/L]: ").lower()
    
    distanciaPercorrida = float(input("Total da distância percorrida: "))
    if(veiculo == 'e'):
        custoKm = distanciaPercorrida * 1.50
        print(f"Você percorreu {distanciaPercorrida} Km e o custo/Km foi de R${custoKm:.2f}")
    elif(veiculo == 'm'):
        custoKm = distanciaPercorrida * 2.25
        print(f"Você percorreu {distanciaPercorrida} Km e o custo/Km foi de R${custoKm:.2f}")
    elif(veiculo == 'l'):
        custoKm = distanciaPercorrida * 3
        print(f"Você percorreu {distanciaPercorrida} Km e o custo/Km foi de R${custoKm:.2f}")

    saida = input("Deseja encerrar o programa? [s/n]: ").lower()
    if(saida == 's'):
            print("Tchau.")
            break
