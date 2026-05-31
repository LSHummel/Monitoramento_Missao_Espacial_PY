
while True:

    print("====================")
    print("       MENU")
    print("====================")
    print("1 - Insira os dados")
    print("2 - Visualisar status")
    print("3 - Executar análise")
    print("4 - Relatório da missão")
    print("5 - SAIR")
    opcao = int(input("Digite o número da opcão que deseja: "))

    match opcao:
        case 1:
            print("----- INSERIR DADOS -----")
            temperatura = float(input("Insira a temperatura da nave em Celsius: "))

            energia = float(input("Insira quanto de energia tem nas baterias em %: "))
            while energia < 0 or energia > 100:
                print("ERRO!")
                energia = float(input("Insira novamente quanto de energia tem nas baterias em %: "))

            potencia_ger = float(input("Insira a potência gerada pelos paineis solares em Watts: "))

            comunicacao = int(input("Digite o status da comunicação (0 = anormal, 1 = normal): "))
            while comunicacao > 1 or comunicacao < 0:
                comunicacao = int(input("Digite o status da comunicação novamente(0 = anormal, 1 = normal): "))

            consumo = float(input("Insira quanta energia foi consumida em Watts: "))


        case 2:
            print("----- STATUS DA MISSÃO -----")
            print(f"Temperatura da nave: {temperatura} C")
            print(f"Porcentagem de energia das baterias: {energia} %")
            print(f"Potência gerada pelos paineis solares: {potencia_ger} W")
            print(f"Status da comunicação: {comunicacao}")
            print(f"Energia consumida: {consumo} W")

        case 3:
            print("----- RSULTADOS DA ANÁLISE -----\n")
            print("Análise da temperatura:")
            if temperatura > 80:
                print("[CRÍTICO]")
                print("!ALERTA DE TEMPERATURA!\n")
            elif temperatura > 90:
                print("[AÇÃO AUTOMÁTICA]")
                print("Ativando sistema de resfriamento...")
            else:
                print("Temperatura normal\n")

            print("Análise da energia:")
            if energia < 20:
                print("[CRÍTICO]")
                print("!ALERTA DE BAIXA ENERGIA!\n")
            elif energia < 15:
                print("[AÇÃO AUTOMÁTICA]")
                print("Desativando módulos secundários...")
                print("Módulo de propulsão funcionando em modo de pouca energia...")
            else:
                print("Energia normal\n")

            print("Análise da comunicação:")
            if comunicacao == 0:
                print("[CRÍTICO]")
                print("!ALERTA DE COMUNICAÇÃO!\n")
                print("[AÇÃO AUTOMÁTICA]")
                print("Tentando reconectar comunicação automaticamente...")
            else:
                print("Comunicação normal\n")

            print("Análise de consumo de energia:")
            if consumo > potencia_ger:
                print("!ALERTA DE DÉFICIT ENERGÉTICO!")
                print("Falhas no nave podem ocorrer")
            else:
                print("Potência normal\n")


        case 4:
            print("=========================================")
            print("    RELATÓRIO DA MISSÃO ESPACIAL")
            print("=========================================\n")
            print(f"Temperatura: {temperatura} C\n")
            print(f"Energia Disponível: {energia} %\n")
            print(f"Potência gerada: {potencia_ger} W\n")
            print(f"Comunicação: {comunicacao}\n")
            print(f"Pôtencia consumida: {consumo} W\n")


        case 5:
            print("FIM DA SIMULAÇÂO")
            break
        case _:
            print("Número inserido invalido!")