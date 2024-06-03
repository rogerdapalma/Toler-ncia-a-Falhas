- O modelo Heartbeat é um dos vários modelos usados em sistemas distribuídos para detectar falhas e garantir a confiabilidade do sistema. Ele implementa um mecanismo simples e eficaz, onde processos enviam periodicamente mensagens "heartbeat" para indicar que estão operacionais. Se um processo não recebe uma mensagem heartbeat dentro de um período de tempo esperado, ele assume que o emissor falhou.

## Como o Heartbeat Funciona

- Envio Periódico de Mensagens: Cada processo no sistema envia mensagens heartbeat periodicamente para outros processos, indicando que está ativo e operacional.
- Detecção de Falhas: Se um processo não recebe uma mensagem heartbeat dentro de um período de tempo específico (timeout), ele assume que o processo que deveria ter enviado a mensagem falhou.
- Repassagem de Mensagens: Quando um processo recebe uma mensagem heartbeat, ele pode repassá-la para seus vizinhos, adicionando sua própria identificação à mensagem, para evitar que mensagens antigas sejam reinseridas na rede.

## Características do Heartbeat

- Simplicidade: É um dos métodos mais simples de detecção de falhas, fácil de implementar e gerenciar.
- Baixa Sobrecarga: O envio periódico de mensagens curtas (heartbeat) gera uma sobrecarga mínima na rede.
- Rapidez na Detecção: Falhas podem ser detectadas rapidamente, dependendo da frequência das mensagens heartbeat e do timeout configurado.
- Comparação com Outros Modelos
- Push Model: Semelhante ao Heartbeat, onde mensagens de controle são enviadas periodicamente pelos processos monitorados.
- Pull Model: Difere do Heartbeat, pois as informações de falha são obtidas por requisição explícita, e não por envio periódico.
- Dual Model: Combina aspectos dos modelos Push e Pull, oferecendo uma abordagem híbrida.
- Gossip Protocol: Dissemina informações através de “fofocas” entre processos, o que pode levar a uma detecção mais distribuída e robusta, mas com maior complexidade de implementação.
