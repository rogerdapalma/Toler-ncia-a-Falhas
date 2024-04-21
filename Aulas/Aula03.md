# Aula 03: Replicação e Redundância

## Informações do Professor
- **Nome**: André Flores dos Santos
- **Local**: Santa Maria – RS, 2024
- **Curso**: Ciência da Computação

## Sumário
1. Introdução
2. Mascaramento de Falhas
3. Redundância
4. Redundância de Hardware e Software

## Mascaramento de Falhas
- O mascaramento de falhas assegura a resposta correta mesmo na presença de falhas.
- Todas as técnicas de tolerância a falhas envolvem alguma forma de redundância.
- O uso de redundância deve ser cuidadosamente ponderado devido ao impacto no custo e desempenho.

## Redundância
- Serve tanto para detecção quanto para mascaramento de falhas.
- Exige mais componentes para mascarar falhas do que para detectá-las.

### Tipos de Redundância
- **Redundância de Informação**: Utiliza bits ou sinais extras para detecção e correção de erros.
- **Redundância Temporal**: Realiza múltiplas execuções da mesma operação para garantir correção.
- **Redundância de Hardware**: Emprega componentes físicos adicionais para garantir continuidade.
- **Redundância de Software**: Utiliza diversidade de software para evitar falhas comuns.

### Exemplos de Redundância de Informação
- **Bit de Paridade**: Usa um bit adicional para verificar a integridade dos dados.
- **Checksum**: Suma de verificação para garantir a integridade dos dados transmitidos.
- **Código de Hamming**: Técnica avançada para detectar e corrigir erros.
- **CRC (Cyclic Redundancy Check)**: Método utilizado para detectar alterações acidentais em dados brutos.

## Exercícios
- **Bit de Paridade**: Verificar a transmissão de mensagens com paridade ímpar.
- **Checksum**: Verificar se as mensagens foram corretamente transmitidas e recebidas.

## Redundância Temporal
- Emprega execuções repetidas para garantir a detecção de falhas, útil onde o tempo não é crítico.

## Redundância de Hardware
- **Redundância Passiva (Estática)**: Usa múltiplos componentes para mascarar falhas.
- **Redundância Ativa (Dinâmica)**: Utiliza técnicas de detecção, localização e recuperação para gerir falhas.

## Redundância de Software
- **Diversidade (Programação de n-versões)**: Implementa múltiplas versões de software para garantir a robustez contra falhas.
- **Blocos de Recuperação**: Utiliza programas secundários que são ativados em caso de falhas.

## Referências Bibliográficas
- SILBERSCHATZ, A. *Sistemas operacionais: conceitos e aplicações*. Addison-Wesley, 2000.
- TANENBAUM, Andrew S.; VAN Steen, Maarten. *Distributed systems: principles and paradigms*. New Jersey: Prentice Hall, 2002.
- WEBER, T. *Tolerância a falhas: conceitos e exemplos*. Disponível em [Link](http://www.inf.ufrgs.br/~taisy/disciplinas/textos/ConceitosDependabilidade.PDF)

## Agradecimentos
- Ao Prof. Guilherme C. Kurtz, Ana Paula
