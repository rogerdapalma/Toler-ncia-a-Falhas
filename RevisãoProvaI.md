# Revisão para Prova de Tolerância a Falhas

## 1. Definições e Conceitos Básicos
- **Falha**: Qualquer condição anormal ou defeito em um componente, equipamento ou subsistema que possa levar a uma falha no sistema.
- **Erro**: Manifestação de uma falha no sistema, que pode levar a comportamentos inadequados do mesmo.
- **Falha (sistema)**: Incapacidade de um sistema ou componente de executar sua função requerida.

## 2. Tipos de Falhas
- **Falhas Transientes**: Ocorrem de forma aleatória e são geralmente causadas por condições externas anômalas.
- **Falhas Intermittentes**: Ocorrem esporadicamente, geralmente devido a falhas nos componentes que se manifestam sob certas condições.
- **Falhas Permanentes**: Continuam a ocorrer até que o componente defeituoso seja reparado ou substituído.

## 3. Tolerância a Falhas
- **Mascaramento de Falhas**: Uso de redundância para ocultar a presença de falhas, garantindo operação contínua na presença de falhas.
- **Redundância**: Emprego de componentes ou sistemas adicionais que permitem a continuidade das operações em caso de falha.

## 4. Tipos de Redundância
- **Redundância de Informação**: Como bits de paridade e códigos de Hamming para detecção e correção de erros.
- **Redundância Temporal**: Realização de múltiplas execuções da mesma operação para garantir a corretude.
- **Redundância de Hardware**: Uso de componentes físicos duplicados para garantir continuidade das operações.
- **Redundância de Software**: Uso de múltiplas versões de software para garantir a corretude das operações.

## 5. Modelos de Falhas
- **Falha por Omissão**: Falha do sistema em responder a entradas.
- **Falha por Resposta**: Sistema responde de maneira incorreta.
- **Falha Arbitrária (ou Bizantina)**: Comportamento completamente irregular e imprevisível do sistema.

## 6. Estratégias para Tolerância a Falhas
- **Diversidade de Design**: Uso de diferentes tecnologias ou abordagens de design para o mesmo componente ou sistema.
- **Detecção de Erros e Recuperação**: Identificação de erros seguida de ações de recuperação ou correção.
- **Failover**: Troca automática para um sistema redundante em caso de falha.

## 7. Conceitos Chave em Métricas de Confiabilidade
- **MTTF (Mean Time to Failure)**: Tempo médio até a primeira falha.
- **MTTR (Mean Time to Repair)**: Tempo médio para reparar um componente falho.
- **MTBF (Mean Time Between Failures)**: Tempo médio entre falhas consecutivas em um sistema reparável.

## 8. Importância da Tolerância a Falhas
- **Sistemas Críticos**: Como sistemas de controle de tráfego aéreo e equipamentos médicos, onde falhas podem ser desastrosas.
- **Sistemas de Alta Disponibilidade**: Como serviços bancários online e plataformas de e-commerce, onde a disponibilidade constante é crucial.

