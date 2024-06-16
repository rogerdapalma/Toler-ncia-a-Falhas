# Relatório de Resultados

## Introdução
Este relatório descreve os resultados obtidos na implementação e teste de um sistema de comunicação entre um servidor e dois clientes, com foco na garantia de entrega de mensagens utilizando mecanismos de confirmação (ACK) e não confirmação (NACK). O sistema foi implementado em Python e os diagramas anexados ilustram o fluxo de mensagens e a lógica de controle.

## Implementação
Os arquivos fornecidos incluem:

- **Server(Emissor).py**: Implementa o servidor que envia mensagens.
- **Client(Receptor).py**: Implementa os clientes que recebem as mensagens.
- **TestesServidor.py**, **TesteDesempenho-Client.py**, **TesteDesempenho-Server.py**: Scripts para testar e medir o desempenho do sistema.
- Diagramas de sequência e de fluxo de controle.

## Fluxo de Mensagens

### Envio de Mensagem:
1. O servidor envia uma mensagem para os clientes.
2. Os clientes recebem a mensagem e verificam a integridade da mesma.

### Confirmação (ACK/NACK):
1. Se a mensagem for recebida corretamente, o cliente envia um ACK (Acknowledgment).
2. Caso contrário, o cliente envia um NACK (Negative Acknowledgment).

### Retransmissão:
1. Se o servidor recebe um NACK, ele retransmite a mensagem.
2. O processo continua até que o cliente envie um ACK, confirmando a recepção correta da mensagem.

## Testes e Resultados
Os testes realizados visaram verificar a robustez do sistema em diferentes condições de rede, incluindo simulações de perda de pacotes e atrasos.

### Resultados dos Testes:
- **Taxa de Retransmissão**: O número de retransmissões foi conforme o esperado, aumentando em cenários com perda de pacotes.
- **Desempenho**: O tempo médio de entrega da mensagem foi medido em diferentes condições de rede. O sistema apresentou um desempenho satisfatório, com um aumento previsível no tempo de entrega em situações de alta perda de pacotes.
- **Consistência**: O sistema garantiu a entrega de mensagens em todas as situações testadas, confirmando a eficácia dos mecanismos de ACK e NACK.

## Diagramas
Os diagramas fornecidos ilustram claramente o fluxo de mensagens e a lógica de controle, facilitando a compreensão do processo de comunicação e os mecanismos de garantia de entrega.

### Diagrama de Sequência:
Mostra a interação entre o servidor e os clientes, destacando o envio de mensagens, confirmações, e retransmissões.

### Diagrama de Fluxo:
Representa a lógica de decisão no cliente, desde a recepção da mensagem até o envio de ACK ou NACK, e a eventual retransmissão da mensagem pelo servidor.

## Possíveis Melhorias

### Otimização da Retransmissão:
Implementar algoritmos de backoff exponencial para gerenciar as retransmissões, reduzindo a carga na rede em caso de alta taxa de perda de pacotes.

### Adaptação às Condições da Rede:
Adaptar dinamicamente os intervalos de timeout e os mecanismos de retransmissão com base nas condições da rede, para melhorar o desempenho.

### Segurança:
Implementar criptografia para garantir a confidencialidade e integridade das mensagens, protegendo contra ataques de interceptação e modificação.

### Escalabilidade:
Avaliar a escalabilidade do sistema em cenários com um número maior de clientes, e otimizar o servidor para gerenciar múltiplas conexões simultâneas de forma eficiente.

## Conclusão
O sistema desenvolvido demonstra uma abordagem eficaz para garantir a entrega de mensagens em um ambiente de rede suscetível a falhas. Os testes confirmam a robustez dos mecanismos de ACK/NACK, e as possíveis melhorias identificadas podem aprimorar ainda mais o desempenho e a segurança do sistema.
