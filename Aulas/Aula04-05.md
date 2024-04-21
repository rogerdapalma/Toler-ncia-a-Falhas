# Aula 04: Resposta Sob Falhas

## Informações do Professor
- **Nome**: André Flores dos Santos
- **Local**: Santa Maria – RS, 2024
- **Curso**: Ciência da Computação

## Respostas sob Falhas
### Controle de Respostas baseado em Redundância
- **Erro**: O Sistema é livre para se comportar.
- **Falha mascarada**: Sem manifestação de erro.
- **Fault Secure**: Baseada em detecção de erro com saídas corretas ou indicação de erro.
- **Fail Safe**: Baseada em detecção de erro com saídas corretas ou estado seguro.

### Fault Secure
- Baseado em detecção de erro.
- Permite operações Fail-Stop (o sistema para em caso de erro).
- Implementação geralmente realizada por redundância de hardware, software ou ambos.

### Fail Safe
- Baseado em detecção de erro.
- Em caso de erro, impede a ativação de certas ações, exemplo: sinal de erro bloqueia as saídas do sistema.

## Tolerância a Falhas: Blocos Básicos de Construção
1. **Consenso**
2. **Armazenamento estável**
3. **Tratadores de falhas**
4. **Detecção e diagnóstico de falhas**
5. **Entrega confiável de mensagens**

### Consenso
- Problema em que um conjunto de processos deve concordar em uma decisão comum.
- Utilizado para ordenação total de eventos, visão consistente dos processos, multicast atômico e confiável.

### Problema de Consenso
- Existe N processos, dos quais f podem falhar.
- Processos devem chegar a um consenso sobre valores corretos apesar das falhas.
- Objetivo é que todos os nós não defeituosos concordem sobre os mesmos valores.

### Modelos de Sistemas
- **Síncronos**: Comportamento temporal conhecido; falhas são detectadas pela ausência de resposta em tempo conhecido.
- **Assíncronos**: Sem conhecimento temporal; falhas não podem ser detectadas pela demora na comunicação.

### Impossibilidades em Modelos Assíncronos
- Demonstrado que o consenso em sistemas assíncronos com a possibilidade de falhas não tem solução.

### Acordo Bizantino
- Trata falhas arbitrárias onde processos podem falhar de maneira complexa, como fornecendo informações falsas.
- Necessário que mais de dois terços dos processos funcionem corretamente para alcançar consenso.

## Atividade para Entregar
- Leia e elabore um resumo sobre “Conceitos em Tolerância a Falhas Bizantinas” e entregue até o final da aula.

## Referências Bibliográficas
- SILBERSCHATZ, A. *Sistemas operacionais: conceitos e aplicações*. Addison-Wesley, 2000.
- TANENBAUM, Andrew S.; VAN Steen, Maarten. *Distributed systems: principles and paradigms*. New Jersey: Prentice Hall, 2002.
- WEBER, T. *Tolerância a falhas: conceitos e exemplos*. Disponível em [Conceitos Dependabilidade](http://www.inf.ufrgs.br/~taisy/disciplinas/textos/ConceitosDependabilidade.PDF)
- LUIZ, A. F. *Protocolos Tolerantes a Faltas Bizantinas para Transações em Bancos de Dados*. Tese de Doutorado, UFSC, 2015. [Link to Thesis](https://repositorio.ufsc.br/bitstream/handle/123456789/134660/334062.pdf?sequence=1&isAllowed=y)

## Agradecimentos
- Ao Prof. Guilherme C. Kurtz, Ana Paula Canal por ter cedido seus materiais que embasaram esta aula.

