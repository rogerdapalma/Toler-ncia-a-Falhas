# Tolerância a Falhas

## Ciência da Computação

### Aula 09

#### Difusão Atômica e Confiável

Santa Maria – RS 2024

Professor: André Flores dos Santos

---

## Confiabilidade

### Problema da Confiabilidade:
- Em muitos casos, os protocolos de difusão não garantem que todos os receptores recebam a mensagem transmitida.
- Isso pode resultar em um estado inconsistente entre os diferentes componentes do sistema.

### Impacto da Inconsistência:
- Inconsistência de estado é particularmente problemática em sistemas que utilizam replicação de dados.
- Por exemplo:
  - Em um sistema de banco de dados replicado, uma atualização (update) enviada a todas as réplicas pode não ser recebida por todas elas.
  - Se uma réplica não recebe a instrução de atualização, ela permanecerá desatualizada, causando inconsistência nos dados.

### Exemplo Prático:
- Imagine um sistema bancário onde várias réplicas do banco de dados mantêm informações de contas correntes.
- Se uma atualização que incrementa o saldo de uma conta for enviada, mas uma das réplicas não receber essa atualização, os saldos exibidos podem divergir.
- Isso pode levar a erros críticos, como saldos incorretos sendo exibidos para os clientes.

### Necessidade de Protocolos Confiáveis:
- Para evitar esses problemas, é essencial utilizar protocolos de difusão confiáveis que garantam a entrega da mensagem a todos os receptores.
- Difusão Atômica: Garante que uma mensagem é entregue a todos ou a nenhum dos receptores.
- Difusão Confiável: Garante que a mensagem é entregue a todos os receptores, mesmo em caso de falhas parciais.

---

## Entrega Confiável de Mensagens

### Conceito de Entrega Confiável:
- Em sistemas distribuídos, é fundamental que as mensagens enviadas por um nó (i) cheguem incorruptas ao nó de destino (j).
- A ordem das mensagens deve ser preservada entre dois nós. Isso significa que se o nó i envia várias mensagens para o nó j, o nó j deve recebê-las na mesma ordem em que foram enviadas.

```css
  [Cliente]
     |
    [m]
     |
 [-----X----]
    /     x
[  Servidor  ]
Difusão Não confiavel
```

```
Cliente1----------------------|´´´´´´´´´´´´´´´´´´´´|
        ..                    |                    |
          ..                  |                    |                     
             ..               |    servidores      |
                ..............|                    |
              .´´´´´´´´´´´´´´´|                    |
           .´´                |                    |
        .´´                   |´´´´´´´´´´´´´´´´´´´                            
Cliente2----------------------|



Difusão sem ordem
```

### Desafios em Sistemas Distribuídos:
- Perda de Mensagens: Mensagens podem ser perdidas devido a falhas na rede ou sobrecarga.
- Erros de Comunicação: Mensagens podem ser corrompidas durante a transmissão.
- Desordem de Mensagens: Mensagens podem chegar fora de ordem devido a diferentes tempos de transmissão ou retransmissão.

### Requisitos para Entrega Confiável:
- Integridade da Mensagem: Uma mensagem enviada por i deve ser recebida corretamente por j, sem alterações.
- Ordem de Entrega: Mensagens enviadas por i devem ser entregues a j na mesma ordem em que foram enviadas.

### Mecanismos para Garantir Confiabilidade:
- Confirmação de Recebimento (ACKs):
  - O nó j envia uma confirmação (acknowledgment) de volta ao nó i para cada mensagem recebida corretamente.
  - Se o nó i não recebe a confirmação em um tempo determinado, ele retransmite a mensagem.
- Numeração Sequencial:
  - Cada mensagem enviada por i é numerada sequencialmente.
  - O nó j utiliza esses números para reordenar as mensagens recebidas e detectar mensagens faltantes.

### Correção de Erros:
- Técnicas como checksums e códigos de correção de erros (ECC) são usadas para detectar e corrigir mensagens corrompidas.

### Protocolos de Transporte Confiável:
- Protocolos como TCP (Transmission Control Protocol) implementam muitos desses mecanismos para garantir a entrega confiável de mensagens.

### Exemplo Prático:
- Comunicação Cliente-Servidor:
  - Em uma aplicação de e-commerce, o servidor deve receber corretamente todas as requisições de compra do cliente e na ordem correta para garantir que as transações sejam processadas adequadamente.

### Desafios em Sistemas Distribuídos
- Difusão Não Confiável: Como mostrado na figura, algumas mensagens podem ser perdidas durante a transmissão.
  - Exemplo: Um cliente envia uma mensagem "m" para vários servidores, mas devido a uma falha na rede, um dos servidores não recebe a mensagem.
- Difusão Sem Ordem: As mensagens podem chegar fora de ordem.
  - Exemplo: Dois clientes enviam mensagens "m1" e "m2" para os mesmos servidores, mas os servidores as recebem em ordens diferentes, causando inconsistência.

---

## Comunicação em Grupo Confiável


```sql
          Emissor
             m
      |----------------|
      |       |        | 
      |       |        |
      |      (x)       |
      |                |
      |                | 
      |                | 
      |               / 
      ----------------|
     |                |
     |                |
     |                |
     |                |
     |                |
     | Grupo Receptor |
     |                |
     |                |
     |                |
     |                |
     |                |
     |                |
     |                |
      ----------------

```
### Implementação de Tolerância a Falhas em Sistemas Distribuídos
- Replicação como Estratégia Principal:
  - A replicação é amplamente utilizada para alcançar tolerância a falhas. Ela envolve a criação de cópias (réplicas) de componentes ou dados em diferentes nós de um sistema distribuído.

### Desafio da Consistência entre Réplicas:
- O maior desafio na replicação é garantir que todas as réplicas permaneçam consistentes. Ou seja, qualquer atualização em uma réplica deve ser refletida em todas as outras réplicas de forma coordenada e sincronizada.
  - Exemplo: Em um banco de dados distribuído, se uma transação atualiza um registro, essa atualização deve aparecer em todas as réplicas do banco de dados.

### Serviço de Difusão Confiável (Reliable Broadcast):
- Para que a replicação funcione corretamente, é necessário um mecanismo que assegure a entrega confiável de mensagens entre os nós do sistema.
- Reliable Broadcast: Este serviço garante que:
  - Entrega Garantida: Todas as réplicas recebem a mensagem, ou nenhuma delas recebe.
  - Integridade da Mensagem: A mensagem recebida é exatamente a mesma que foi enviada, sem alterações.
  - Ordem Consistente: Todas as réplicas recebem as mensagens na mesma ordem.

### Benefícios da Comunicação Confiável
- Resiliência a Falhas:
  - Mesmo que alguns nós falhem, as réplicas restantes podem continuar a operar, assegurando a disponibilidade do sistema.
- Disponibilidade e Confiabilidade:
  - Com réplicas consistentes, o sistema pode atender requisições de leitura e escrita de forma eficiente, mesmo sob condições adversas.

---

## Difusão Confiável Clássica

### Definição:
- Difusão confiável (ou broadcast confiável) é um protocolo de comunicação em sistemas distribuídos onde a entrega de mensagens deve ser garantida de maneira confiável para todos os nós participantes.

### Considerações:
- Considere que o ambiente ofereça uma comunicação multicast não confiável, o que significa que uma mensagem pode se perder e ser entregue somente a alguns.
- O remetente possui um History Buffer e quando um receptor detectar a falta de uma mensagem (receber M25 sem o M24) ou passar um tempo (timeout) sem o emissor receber a confirmação, a mensagem é retransmitida.
### A
```lua
Receptor acusou
falta da mensagem n. 24

Remetente
+-----------+
|           |
| M25       |
|           |
| +-------+ |
| |       | |
| | Buffer| |
| | de    | |
| | histórico|
| |       | |
| +-------+ |
+-----------+
    |
    |
  Rede
    |
    |
+-----------+  +-----------+  +-----------+  +-----------+
| Receptor  |  | Receptor  |  | Receptor  |  | Receptor  |
| Último = 24| | Último = 24| | Último = 23| | Último = 24|
|           |  |           |  |           |  |           |
| M25       |  | M25       |  | M25       |  | M25       |
+-----------+  +-----------+  +-----------+  +-----------+

```

### B
```lua
Remetente
+-----------+
|           |
| M25       |
|           |
| +-------+ |
| |       | |
| | Buffer| |
| | de    | |
| | histórico|
| |       | |
| +-------+ |
+-----------+
    |
    |
  Rede
    |
    |
+-----------+  +-----------+  +-----------+  +-----------+
| Receptor  |  | Receptor  |  | Receptor  |  | Receptor  |
| Último = 25| | Último = 25| | Último = 23| | Último = 25|
|           |  |           |  |           |  |           |
| M25       |  | M25       |  | M25       |  | M25       |
+-----------+  +-----------+  +-----------+  +-----------+
    |
    |
  Rede
    |
    |
+-----------+  +-----------+  +-----------+  +-----------+
|           |  |           |  |           |  |           |
|  ACK 25   |  |  ACK 25   |  |           |  |  ACK 25   |
+-----------+  +-----------+  +-----------+  +-----------+

Acusou falta de 24
```

### Difusão Confiável: baseada em ACK
- **Acknowledgement (ACK)**
  - Considerando que os processos não apresentam falhas e que o grupo permanece constante, a implementação de difusão confiável é simples:
    - Cada mensagem é carimbada com um número de sequência.
    - O processo que origina a mensagem deve mantê-la em um buffer até que seja recebido um ACK de todos os outros processos.
    - Caso o originador não receba o ACK de todos os destinatários, ele retransmite a mensagem.
    - Caso um receptor note que foi perdida uma mensagem da sequência, ele pede uma retransmissão.

### Problemas com Soluções Baseadas em ACK
- **Implosão de ACK:**
  - Em um sistema com N receptores, cada receptor envia um ACK (acknowledgment) para confirmar a recepção da mensagem.
  - Isso resulta em N mensagens de ACK trafegando na rede, causando um problema conhecido como implosão de retorno.
  - A sobrecarga de mensagens ACK pode levar à saturação da rede, diminuindo a eficiência e aumentando a latência.

- **Falha do Emissor:**
  - Se o emissor cair depois de enviar a primeira transmissão, a correção de erros torna-se problemática.
  - Normalmente, a correção de erros é feita pelo emissor, mas se ele não estiver disponível, a recuperação torna-se difícil.

---

## Controle de Feedback Não Hierárquico: baseado em NACK

### Solução com Controle de Feedback:
- Para resolver o problema, a solução com controle de feedback estabelece que ao invés de enviar um ACK de confirmação, o destinatário envie um NACK (Negative Acknowledgment) para todo o grupo caso ele detecte a perda de uma mensagem.
  - Isso significa que nas execuções com sucesso, nenhuma mensagem de retorno será necessária.
- O multicast de NACK permite que outro membro do grupo supra a perda de uma mensagem e não necessariamente o emissor.

### Evitar a Explosão de Retransmissões:
- Para evitar que mais de um destinatário envie um NACK, um destinatário deve esperar um tempo aleatório antes de enviar um NACK.
- Se durante este tempo o destinatário receber um NACK de outro destinatário, ele não precisa mais enviar o seu NACK, pois a mensagem vai ser retransmitida.

### Problemas:
- O problema é que o originador terá que manter a mensagem no seu buffer por tempo indeterminado (a qualquer momento um destinatário pode pedir uma retransmissão).
- Outro problema é que cada mensagem de NACK é transmitida para todos os outros processos (todos têm que interromper o que estão fazendo para ler a mensagem).
- Além disso, para garantir que somente um NACK será enviado quando vários processos notarem a falta de uma mensagem, deve-se manter uma sincronia.

### Aprimoramento:
- Permitir que os receptores possam ajudar na recuperação local, ou seja, se um receptor que recebeu uma mensagem m com sucesso, observar que outro processo não recebeu, ele mesmo poderá retransmitir m.
- Daí surge outro problema, que é em relação ao processo que irá suprir a falta da mensagem. Como garantir que somente um processo retransmita?

---

## Controle de Feedback Hierárquico

### Solução para Escalabilidade:
- Para resolver o problema de escalabilidade em grupos com um grande número de membros, a alternativa é utilizar um controle de Feedback Hierárquico.
- Cada subgrupo forma um nó da árvore hierárquica, onde o subgrupo o qual pertence o emissor (originador) é o nó raiz.
- Cada subgrupo contém um coordenador local responsável por gerenciar as requisições por retransmissão. Ele possui um buffer com um histórico, caso ele necessite requisitar uma nova retransmissão para uma determinada mensagem.
- Dentro de cada subgrupo pode-se utilizar um esquema particular de multicast.

---

## Difusão Atômica

### Considerações:
- Os casos anteriores discutidos garantem um bom funcionamento somente se não houver falhas nos processos.
- A difusão atômica (Atomic Multicast) garante a entrega atômica das mensagens pelos processos na mesma ordem.

### Cenário:
- Imagine que um processo (réplica de banco de dados) mande uma mensagem para que todos os outros processos atualizem os seus dados.
- Uma destas réplicas sofre algum dano e fica temporariamente inoperante.
- Ao se recuperar, essa réplica está inconsistente, pois durante o tempo que ficou inoperante ela perdeu algumas mensagens de atualização.

### Garantia da Difusão Atômica:
- A difusão atômica garante que a operação de atualização que foi enviada a todas as réplicas um pouco antes de uma delas cair ou é executada em todas as réplicas não faltosas ou em nenhuma.
- A atualização é realizada se as réplicas restantes concordarem que a réplica que caiu não pertence mais ao grupo.
- Após a recuperação, a réplica é validada como sendo do grupo e recebe as atualizações.

### Sincronia Virtual:
- Todos os processos de um grupo devem concordar em quem são os integrantes deste grupo.
- Se o grupo muda quando uma mensagem está trafegando na rede, esta mensagem deve ser entregue a todos os membros do grupo antes que este mude. Caso contrário, a mensagem deve ser descartada.
- A vantagem disso é que uma mensagem somente é entregue para todos os membros de um grupo ou para nenhum deles, evitando inconsistências.

---

## Difusão Atômica: Ordenando Mensagens

### Tipos de Ordenamento:
- **Multicast desordenado:** Não apresenta garantias de ordenação de mensagens.
- **Multicast com ordenação FIFO:** As mensagens de um mesmo processo são entregues na mesma ordem. Não há garantias sobre a ordenação entre diferentes processos.
- **Multicast com ordenação por causalidade:** As mensagens são entregues preservando-se as relações de causalidades. Se m4 é consequência de m2 então todos devem receber m2 antes de m4.
- **Multicast totalmente ordenado:** É a forma mais forte de ordenamento. O protocolo requer que quando as mensagens são entregues, elas devem ser entregues na mesma ordem para todos os membros do grupo, independentemente se a entrega da mensagem for não ordenada, ordenada em FIFO ou ordenada por causalidade.

---

## TRABALHO FINAL

- Disponível no Moodle UFN.

---

## Referências Bibliográficas

- SILBERSCHATZ, A. Sistemas operacionais: conceitos e aplicações. Addison-Wesley, 2000.
- TANENBAUM, Andrew S.; VAN Steen, Maarten. Distributed systems: principles and paradigms. New Jersey: Prentice Hall, 2002.
- WEBER, T. Tolerância a falhas: conceitos e exemplos. Disponível em [ConceitosDependabilidade.PDF](http://www.inf.ufrgs.br/~taisy/disciplinas/textos/ConceitosDependabilidade.PDF)
- SANTOS, F, André. Hardware Fault Tolerance Techniques. Disponível em [hdl.handle.net/10183/178392](http://hdl.handle.net/10183/178392)

---

## Agradecimentos

- Ao Prof. Guilherme C. Kurtz, Ana Paula Canal por ter cedido seus materiais que embasaram esta aula.

---

Santa Maria – RS 2024

Email: andre.flores@ufn.edu.br
