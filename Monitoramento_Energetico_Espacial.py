# FUNÇÕES DE VERIFICAÇÃO E ALERTA

# TEMPERATURA
def verif_temp(temperatura):
    if temperatura > 90:
        print("\033[33m[CRÍTICO]\033[0m")
        print("\033[33m!ALERTA DE TEMPERATURA!\033[0m\n\n")
        print("\033[33m[AÇÃO AUTOMÁTICA]\033[0m")
        print("\033[33mAtivando sistema de resfriamento...\033[0m\n\n")
    elif temperatura > 80:
        print("\033[33m[CRÍTICO]\033[0m")
        print("\033[33m!ALERTA DE TEMPERATURA!\033[0m\n\n")

    else:
        print("\033[32mTemperatura normal\033[0m\n\n")

def alerta_temp(temperatura):
    if temperatura > 90:
        return 2
    elif temperatura > 80:
        return 1
    else:
        return 0


# ENERGIA
def verif_ener(energia):
    if energia < 15:
        print("\033[33m[CRÍTICO]\033[0m")
        print("\033[33m!ALERTA DE BAIXA ENERGIA!\033[0m\n\n")
        print("\033[33m[AÇÃO AUTOMÁTICA]\033[0m")
        print("\033[33mDesativando módulos secundários...\033[0m")
        print("\033[33mMódulo de propulsão funcionando em modo de pouca energia...\033[0m\n\n")
    elif energia < 20:
        print("\033[33m[CRÍTICO]\033[0m")
        print("\033[33m!ALERTA DE BAIXA ENERGIA!\033[0m\n\n")

    else:
        print("\033[32mEnergia normal\033[0m\n\n")

def alerta_ener(energia):
    if energia < 15:
        return 2
    elif energia < 20:
        return 1
    else:
        return 0


# COMUNICAÇÃO
def verif_comuni(comunicacao):
    if comunicacao == 0:
        print("\033[33m[CRÍTICO]\033[0m")
        print("\033[33m!ALERTA DE COMUNICAÇÃO!\033[0m\n\n")
        print("\033[33m[AÇÃO AUTOMÁTICA]\033[0m")
        print("\033[33mTentando reconectar comunicação automaticamente...\033[0m\n\n")
    else:
        print("\033[32mComunicação normal\033[0m\n\n")

def alerta_comuni(comunicacao):
    if comunicacao == 0:
        return 0
    else:
        return 1


# CONSUMO DE ENERGIA
def verif_consumo(consumo, potencia_ger):
    if consumo > potencia_ger:
        print("\033[33m!ALERTA DE DÉFICIT ENERGÉTICO!\033[0m")
        print("\033[33mFalhas no nave podem ocorrer\033[0m\n\n")
    else:
        print("\033[32mConsumo normal\033[0m\n\n")

def alerta_consumo(consumo, potencia_ger):
    if consumo > potencia_ger:
        return 1
    else:
        return 0

# CRIAR ARQUIVO .JASON
def salvar_dados(temperatura, energia, consumo, potencia_ger, comunicacao):
    import json
    import os

    novo_registro = {
        "temperatura": temperatura,
        "energia": energia,
        "consumo": consumo,
        "potencia_gerada": potencia_ger,
        "comunicacao": comunicacao
    }

    # Verifica se o arquivo já existe
    if os.path.exists("missao.json"):

        try:
            with open("missao.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

        except json.JSONDecodeError:
            dados = []

    else:
        dados = []

    # Adiciona o novo registro ao histórico
    dados.append(novo_registro)

    # Salva novamente o arquivo
    with open("missao.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)




# CÓDIGO PRINCIPAL
while True:
    # MENU
    print("\n====================")
    print("       MENU")
    print("====================")
    print("1 - Insira os dados")
    print("2 - Visualisar status")
    print("3 - Executar análise")
    print("4 - Relatório da missão")
    print("5 - SAIR")
    opcao = int(input("Digite o número da opcão que deseja: "))

    match opcao:
        # INSERIR DADOS
        case 1:
            print("\n----- INSERIR DADOS -----\n")
            temperatura = float(input("Insira a temperatura dos módulos em Celsius: "))

            energia = int(input("Insira quanto de energia tem nas baterias em %: "))
            while energia < 0 or energia > 100:
                print("ERRO!")
                energia = int(input("Insira novamente quanto de energia tem nas baterias em %: "))

            potencia_ger = float(input("Insira a potência gerada pelos paineis solares em Watts: "))

            consumo = float(input("Insira quanta energia foi consumida em Watts: "))

            comunicacao = int(input("Digite o status da comunicação (0 = anormal, 1 = normal): "))
            while comunicacao > 1 or comunicacao < 0:
                comunicacao = int(input("Digite o status da comunicação novamente(0 = anormal, 1 = normal): "))

            print("Salvando dados...")
            salvar_dados(temperatura, energia, consumo, potencia_ger, comunicacao)
            print("Dados salvo com sucesso!")


        # STATUS DA MISSÃO
        case 2:
            print("\n----- STATUS DA MISSÃO -----\n")
            print(f"Temperatura dos módulos: {temperatura} C")
            print(f"Porcentagem de energia das baterias: {energia} %")
            print(f"Potência gerada pelos paineis solares: {potencia_ger} W")
            print(f"Energia consumida: {consumo} W")
            print(f"Status da comunicação: {comunicacao}")


        # RESULTADOS DA ANÁLISE
        case 3:
            print("----- RSULTADOS DA ANÁLISE -----\n")
            print("Análise da temperatura:")
            verif_temp(temperatura)

            print("Análise da energia:")
            verif_ener(energia)

            print("Análise de consumo de energia:")
            verif_consumo(consumo, potencia_ger)

            print("Análise da comunicação:")
            verif_comuni(comunicacao)



        # RELATÓRIO
        case 4:
            print("\n=========================================")
            print("    RELATÓRIO DA MISSÃO ESPACIAL")
            print("=========================================\n")
            print(f"Temperatura: {temperatura} C\n")
            print(f"Energia Disponível: {energia} %\n")
            print(f"Potência gerada: {potencia_ger} W\n")
            print(f"Pôtencia consumida: {consumo} W\n")
            print(f"Comunicação: {comunicacao}\n")
            print("------------------------------------------")
            if alerta_temp(temperatura) == 0 and alerta_comuni(comunicacao) == 1 and alerta_ener(energia) == 0 and alerta_consumo(consumo, potencia_ger) == 0:
                print("STATUS GERAL: \033[32mNORMAL\033[0m")
            elif alerta_temp(temperatura) == 1 or alerta_temp(temperatura) == 2 or alerta_comuni(comunicacao) == 0 or alerta_ener(energia) == 1 or alerta_ener(energia) == 2 or alerta_consumo(consumo, potencia_ger) == 1:
                print("STATUS GERAL: \033[33mCRÍTICO\033[0m")
            print("------------------------------------------\n")

            # ALERTAS
            if alerta_temp(temperatura) == 1 or alerta_temp(temperatura) == 2:
                print("\033[33m[CRÍTICO] Temperatura Elevada\033[0m\n")
            if alerta_ener(energia) == 1 or alerta_ener(energia) == 2:
                print("\033[33m[CRÍTICO] Energia Baixa\033[0m\n")
            if alerta_consumo(consumo, potencia_ger) == 1:
                print("\033[33m[CRÍTICO] Consumo Elevado\033[0m\n")
            if alerta_comuni(comunicacao) == 0:
                print("\033[33m[CRÍTICO] Comunicação Perdida\033[0m\n")

            # AÇÕES AUTOMÁTICAS
            if alerta_temp(temperatura) == 2 or alerta_comuni(comunicacao) == 0 or alerta_ener(energia) == 2 or alerta_consumo(consumo, potencia_ger) == 1:
                print("ATIVANDO AÇÕES AUTOMÁTICAS...\033[0m\n")

            if alerta_temp(temperatura) == 2:
                print("\033[33m[TEMPERATURA] Ativando sistema de resfriamento...\033[0m\n")
            if alerta_ener(energia) == 2:
                print("\033[33m[ENERGIA] Desativando módulos secundários...")
                print("\033[33mMódulo de propulsão funcionando em modo de pouca energia...\033[0m\n")
            if alerta_comuni(comunicacao) == 0:
                print("\033[33m[COMUNICAÇÃO] Tentando reconectar comunicação automaticamente...\033[0m\n")




        case 5:
            print("FIM DA SIMULAÇÂO")
            break
        case _:
            print("Número inserido invalido!")