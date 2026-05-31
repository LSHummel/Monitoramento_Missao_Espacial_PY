# Sistema Inteligente de Monitoramento de Missão Espacial

## Descrição

Este projeto simula um sistema de monitoramento para uma missão espacial experimental de uma nave que possui abastecimento energético de paineis solares implementados em sua estrutura e com baterias para armazenar a energia gerada. O programa recebe dados operacionais da nave, realiza análises automáticas e gera alertas quando situações críticas são detectadas.

Os dados monitorados incluem temperatura dos módulos, nível de energia das baterias, potência gerada pelos painéis solares, consumo energético e status da comunicação.

## Funcionalidades

* Cadastro de dados da missão.
* Monitoramento da temperatura dos módulos.
* Monitoramento do nível de energia das baterias.
* Verificação do consumo energético.
* Monitoramento do sistema de comunicação.
* Geração automática de alertas críticos.
* Execução de ações automáticas em situações de risco.
* Geração de relatórios da missão.
* Armazenamento dos dados em arquivo JSON.

## Alertas Implementados

### Temperatura

* Acima de 80°C: alerta crítico.
* Acima de 90°C: alerta crítico e ativação automática do sistema de resfriamento.

### Energia

* Abaixo de 20%: alerta crítico.
* Abaixo de 15%: alerta crítico e ativação do modo de economia de energia.

### Comunicação

* Comunicação inativa: alerta crítico e tentativa automática de reconexão.

### Consumo Energético

* Consumo maior que a potência gerada: alerta de déficit energético.

## Arquivo de Dados

As informações inseridas pelo usuário são armazenadas no arquivo `missao.json`, permitindo manter um histórico dos registros realizados durante as simulações.

