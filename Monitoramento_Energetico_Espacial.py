
while True:

    print("====================")
    print("       MENU")
    print("====================")
    print("1 - Insira os dados")
    print("2 - Visualisar status")
    print("3 - Executar analise")
    print("4 - Relatório da missão")
    print("5 - SAIR")
    opcao = int(input("Digite o número da opcão que deseja: "))

    match opcao:
        case 1:
            print("----- INSERIR DADOS -----")
            temperatura = float(input("Insira a temperatura da nave em Celcius: "))
            energia = float(input("Insira quanto de energia tem nas baterias em %: "))
            potencia_ger = float(input("Insira a potencia gerada pelos paineis solares em Wats: "))
            comunicacao = int(input("Digite o status da comunicacao (0 = anormal, 1 = normal): "))
            consumo = float(input("Insira quanta energia foi consumida em Wats: "))


        case 2:
            print(f"Temperatura da nave: {temperatura} C")
            print(f"Porcentagem de energia das baterias: {energia} %")
            print(f"Potencia gerada pelos paineis solares: {potencia_ger} W")
            print(f"Status da comunicacao: {comunicacao}")
            print(f"Energia consumida: {consumo} W")

        case 3:
            print("opcao 3")

        case 4:
            print("opcao 4")

        case 5:
            print("FIM DA SIMULAÇÂO")
            break
        case _:
            print("Número inserido invalido!")