# Aula 02: Aplicações de Sistemas Tolerantes a Falhas

## Informações do Professor

- **Nome**: André Flores dos Santos
- **Curso**: Ciência da Computação
- **Local**: Santa Maria – RS, 2024

## Sumário

1. Introdução
2. Aplicações de Sistemas Tolerantes a Falhas (STF)
3. Modelos de Falhas em Sistemas Distribuídos
4. Modelos de Falhas em Hardware
5. Exemplos
6. Exercícios

## Aplicações de Sistemas Tolerantes a Falhas

- Técnicas para construir sistemas confiáveis e sempre disponíveis envolvem uso de redundância.
- Redundância aumenta o custo, necessitando uma clara definição de custo-benefício.
- Aplicações críticas incluem medicina, controle de processos, transportes aéreos, sistemas de tempo real, telefonia, sistemas de transação e redes locais.

## Modelos de Falhas em Sistemas Distribuídos

### Tipos de Falhas

- **Falha por colapso (crash)**
  - O sistema deixa de responder após uma falha até ser reinicializado.
  - Exemplo: Sistema operacional que para de funcionar.

- **Falha por omissão (omission)**
  - Falha em responder a entradas, incluindo omissão de recebimento e envio de mensagens.

- **Falha por temporização (timing)**
  - Resposta fora do intervalo de tempo especificado, comum em sistemas de tempo real.

- **Falha de resposta**
  - O componente responde de forma incorreta, produzindo saída errada.

- **Falha arbitrária (bizantina)**
  - Comportamento completamente arbitrário do sistema, produzindo saídas inesperadas.

### Implementação em Python

- Implementações de simulações de falhas (crash, omission, timing) em Python para entender melhor cada tipo de falha.

## Classificação de Falhas em Hardware

- **Transientes**: Ocorrem uma vez e desaparecem, como perdas de bits devido a condições meteorológicas.
- **Intermitentes**: Ocorrem várias vezes e são difíceis de detectar.
- **Permanentes**: Continuam até que o componente falho seja substituído.

## Exercícios Propostos

1. Implementar e entregar algoritmos de simulação das falhas discutidas.
2. Procurar exemplos reais de falhas em sistemas críticos e discutir na próxima aula.

## Agradecimentos

- Agradecimentos ao Prof. Guilherme C. Kurtz e Ana Paula Canal por seus materiais.

## Referências Bibliográficas

- SILBERSCHATZ, A. *Sistemas operacionais: conceitos e aplicações*. Addison-Wesley, 2000.
- WEBER, T. *Tolerância a falhas: conceitos e exemplos*. Disponível em [Link](http://www.inf.ufrgs.br/~taisy/disciplinas/textos/ConceitosDependabilidade.PDF)

