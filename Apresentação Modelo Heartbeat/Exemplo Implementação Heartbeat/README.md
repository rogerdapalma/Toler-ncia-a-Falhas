# Heartbeat Detector
Este projeto implementa um detector de defeitos simples usando o modelo de heartbeat. O modelo de heartbeat é uma técnica usada para monitorar a saúde de sistemas distribuídos. Neste exemplo, um componente envia regularmente "batimentos cardíacos" (heartbeats) para outro componente para indicar que está funcionando corretamente. Se um batimento cardíaco não é recebido dentro de um limite de tempo, uma falha é detectada.

## Funcionalidades
- Envio periódico de heartbeats.
- Detecção de falhas se um heartbeat não for recebido dentro de um intervalo de tempo especificado.
- Execução de procedimentos de recuperação em caso de falha.
- Força uma falha após um número específico de heartbeats para simulação de falhas.
## Estrutura do Código
O código está organizado da seguinte forma:

- `HEARTBEAT_INTERVAL`: Intervalo de tempo entre os heartbeats (em segundos).
- `DETECTION_THRESHOLD`: Tempo limite para detecção de falhas (em segundos).
- `FORCE_FAILURE_AFTER`: Número de heartbeats antes de forçar uma falha (para simulação de falhas).
## Classe HeartbeatDetector
- ``__init__(self)``: Inicializa a classe com um evento para monitorar heartbeats e variáveis de controle de execução.
- ``start(self)``: Inicia as threads para envio de heartbeats e detecção de falhas.
- ``start_heartbeat(self)``: Inicia uma thread que envia heartbeats a cada intervalo definido.
- ``send_heartbeat(self)``: Simula o envio de um heartbeat e define o evento indicando que o heartbeat foi enviado. Força uma falha após um número específico de heartbeats.
- ``start_detection(self)``: Inicia a detecção de falhas, verificando periodicamente se heartbeats foram recebidos.
- ``check_heartbeat(self)``: Verifica se um heartbeat foi recebido. Se não, detecta uma falha e chama o tratamento de falha.
- ``handle_failure(self)``: Lida com a falha e interrompe a execução do detector.
## Execução
Para executar o código, basta rodar o script principal. O sistema simulará o envio de heartbeats e a detecção de falhas.

```
python heartbeat_detector.py
```

O código continuará em execução até que uma falha seja detectada ou uma interrupção (Ctrl+C) ocorra. Após FORCE_FAILURE_AFTER heartbeats, o sistema simulará uma falha, e a detecção de falhas será ativada.

Exemplo de Saída
```
Enviando heartbeat...
Heartbeat recebido. Sistema está saudável.
Enviando heartbeat...
Heartbeat recebido. Sistema está saudável.
Enviando heartbeat...
Heartbeat recebido. Sistema está saudável.
Enviando heartbeat...
Heartbeat recebido. Sistema está saudável.
Enviando heartbeat...
Heartbeat recebido. Sistema está saudável.
Erro forçado: heartbeat não enviado.
Falha detectada! Heartbeat não recebido.
Executando procedimentos de recuperação...

```

Neste exemplo, após 5 heartbeats, um erro é forçado, resultando na detecção de falha e execução de procedimentos de recuperação.