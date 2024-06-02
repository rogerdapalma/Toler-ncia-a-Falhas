# Tolerância a Falhas

## Ciência da Computação

**Aula 08 Parte II**  
Detectores de Defeitos  

Santa Maria – RS 2024  

Professor: André Flores dos Santos

## Introdução

A norma ISO/IEC 9126 (trocada por [ISO 25000 Standards](https://iso25000.com/index.php/en/iso-25000-standards) ou [ABNT Catálogo](https://www.abntcatalogo.com.br/pnm.aspx?Q=djlvb3N4RnVvWEJPQUlWRGtTWFYwT1h2dnc2M0dkNzV0V09NRjRMZWFTZz0=)) regulamenta a qualidade de produto de software:

- **Funcionalidade**: atender aos requisitos do usuário por meio das funcionalidades.
- **Usabilidade**: software compreendido, funcionamento aprendido, ser operável pelo usuário.
- **Eficiência**: tempo de execução compatível.
- **Manutenibilidade**: capacidade do produto ser modificado.
- **Portabilidade**: capacidade do sistema ser transferido de um ambiente para outro.
- **Dependabilidade**: capacidade dos sistemas computacionais de prestar um serviço que se pode justificadamente confiar.

## Técnicas de Tolerância a Falhas

Diversas técnicas de TF foram propostas: Redundância, Atualização e restauração de estados consistentes, Comunicação em grupo confiável.

Sistemas tolerantes a falhas partem do princípio de replicação de componentes e/ou recursos.

Entretanto, com a replicação, há outros problemas que devem ser tratados. Por exemplo:
- Fazer com que eventos sejam executados na mesma sequência em todas as réplicas do sistema.

## Impossibilidade FLP

Impossibilidade FLP (Fischer, Lynch, and Paterson impossibility) é a impossibilidade de diferenciar um processo falho de um processo mais lento.

### O que é?

Não há como garantir o cumprimento das propriedades de um protocolo de consenso em um sistema distribuído assíncrono que esteja sujeito até mesmo a uma única falha por colapso (situação em que um processo em um sistema distribuído deixa de funcionar permanentemente).

### Motivo

Na ausência de resposta de um ou mais processos, os demais participantes do consenso não conseguem identificar se houve uma falha ou se o processo está apenas mais lento que o normal.

### O que isso irá causar?

Os participantes do consenso iriam esperar infinitamente pela resposta do processo falho.

### Solução

Um sistema assíncrono auxiliado por um detector de defeitos possibilitará a resolução de um consenso. Cada processo tem acesso a um módulo de DF local que monitora os processos do sistema, mantendo uma lista de processos suspeitos.

Os módulos de DF não são confiáveis, podendo adicionar um processo ‘p’ à lista de suspeitos mesmo que ele esteja funcionando normalmente. Se em um outro momento o módulo concluir que a suspeita sobre ‘p’ era um engano, ele pode ser retirado da lista de suspeitos.

## Definição de um modelo

- Um sistema distribuído constituído de N processos (p1, p2, ..., pN).
- Os processos são conectados por um canal confiável.
- Os processos só podem falhar por colapso (crash).

### Propriedades dos Detectores de Defeitos

#### Completeness

- **Strong Completeness**: em um tempo finito, todos processos que falharam serão permanentemente suspeitos por todos processos corretos.
- **Weak Completeness**: em um tempo finito, todos processos que falharam serão permanentemente suspeitos por alguns processos corretos.

#### Accuracy

- **Strong Accuracy**: nenhum processo é considerado suspeito antes de ter falhado.
- **Weak Accuracy**: existe pelo menos um processo correto que jamais torna-se suspeito de falha.
- **Eventual Strong Accuracy**: existe um instante após o qual processos corretos não são considerados suspeitos por nenhum processo correto.
- **Eventual Weak Accuracy**: existe um instante após o qual algum processo correto não é considerado suspeito por nenhum processo correto.

## Modelos de Detectores de Defeitos

### Modelo Push

No algoritmo de detecção Push, as mensagens de controles geradas pelos detectores seguem o mesmo sentido do fluxo das informações. Os processos monitorados por um detector de defeitos enviam periodicamente uma mensagem Heartbeat indicando que ainda estão operacionais.

### Modelo Pull

No detector de defeitos Pull, o fluxo de informações segue em sentido oposto ao fluxo de controle. As informações do detector de defeitos só são obtidas através da requisição junto aos processos monitorados. Os processos monitorados enviam respostas apenas quando questionados pelo detector.

### Modelo Dual

O modelo dual combina os modelos Push e Pull, podendo ser utilizados ao mesmo tempo. Inicialmente, utiliza-se o modelo Push, e após um certo tempo, o modelo Pull é adotado para os processos que não enviaram mensagens Heartbeat.

### Detector Gossip

O protocolo Gossip dissemina a informação por meio de “fofocas” (gossip), onde a cada informação nova que um processo recebe, ele conta para os seus vizinhos. Cada um dos processos mantém uma lista contendo o endereço de cada processo, um contador heartbeat, e um temporizador.

### Modelo Heartbeat

No modelo Heartbeat, as mensagens enviadas são do tipo Heartbeat, anexadas a um identificador do processo emissor e receptor. Quando um processo recebe uma mensagem Heartbeat, ele a repassa para seus vizinhos, acrescentando sua própria identificação à mensagem, evitando que uma mensagem antiga seja reinserida na rede.

## Trabalho II – Nota 02

1. Foram trabalhados alguns modelos de detectores de defeitos. Faça uma pesquisa por um modelo de detector de defeitos e apresente em um artigo científico publicado em revista ou anais de eventos. Caracterize o detector de defeitos escolhido e relacione-o aos modelos estudados.
2. Fazer um resumo para entregar em arquivo ‘nome.docx’ com as explicações, o arquivo do artigo encontrado ‘pdf’ e sua referência bibliográfica (link para download).
3. Fazer uma apresentação de slides para apresentar para os colegas e o professor para a próxima aula.

OBS: Trabalho Individual, se entregar com atraso a nota será reduzida pela metade.
