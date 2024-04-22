# LISTA DE EXERCÍCIOS - REVISÃO PARA A PROVA 01. TOLERÂNCIA A FALHAS
## CIÊNCIA DA COMPUTAÇÃO, UNIVERSIDADE FRANCISCANA – UFN – 2024-01

**PROFESSOR:** André F. dos Santos

**Nome do aluno:** 

**Data:** 

---

### 1) Como podemos definir uma falha, através de que parâmetros?

Uma falha em sistemas computacionais pode ser definida através dos seguintes parâmetros:

- **Natureza da Falha:** Tipo de falha, como falhas de hardware, software ou operacionais.
- **Escopo da Falha:** Se afeta uma parte isolada ou todo o sistema.
- **Duração da Falha:** Quanto tempo a falha persiste, seja transitória ou permanente.
- **Efeito da Falha:** Impacto no funcionamento do sistema, como perda de dados ou interrupção das operações.
- **Visibilidade da Falha:** Se a falha é óbvia para os usuários ou requer monitoramento específico para ser detectada.
- **Reprodutibilidade:** Se a falha pode ser repetida sob as mesmas condições.

---

### 2) Descreva a diferença entre falha, erro e defeito?

- **Defeito:** É basicamente um problema no código ou design do sistema. É o ponto inicial que pode levar a um erro.
- **Erro:** Refere-se ao estado do sistema que é a consequência direta de um defeito. Pode não ser imediatamente perceptível.
- **Falha:** Acontece quando o erro se manifesta de forma a afetar o desempenho, a funcionalidade ou a operação do sistema.

---

### 3) Escolha dois atributos da dependabilidade para conceituar e exemplificar:

- **Confiabilidade:** Descreve a capacidade do sistema de funcionar corretamente durante um período determinado. Exemplo: sistema de freios de carro.
- **Disponibilidade:** Refere à capacidade do sistema estar acessível e funcional quando necessário. Exemplo: serviço de streaming de vídeo.

---

### 4) Diferencie MTTF, MTTR, MTBF:

- **MTTF (Mean Time to Failure):** Tempo médio até a primeira falha de um componente. Exemplo: lâmpadas.
- **MTTR (Mean Time to Repair):** Tempo médio necessário para reparar um componente após uma falha. Exemplo: servidor de computador.
- **MTBF (Mean Time Between Failures):** Tempo médio entre falhas de um sistema que pode ser reparado. Exemplo: linha de montagem automatizada.

---

### 5) Como o paradigma de tolerância a falhas pode ser definido?

O paradigma de tolerância a falhas refere-se à capacidade de um sistema continuar operando adequadamente na presença de falhas, usando redundâncias, verificações de erros, e sistemas que automaticamente corrigem ou contornam problemas.

---

### 6) Quais são algumas das técnicas de tolerância a falhas utilizadas em sistemas computacionais para recuperação?

- **a) Monitoramento de tráfego, detecção de intrusos e firewall de última geração**
- **b) Resiliência, criptografia avançada e segurança por obscuridade**
- **c) Indexação, compactação de dados e escalonamento de processos**
- **d) Mascaramento de falhas, detecção de falhas, localização, confinamento, recuperação, reconfiguração e tratamento**
- **e) Redundância de hardware, criptografia de dados e replicação de servidores**

---

### 7) No que consiste o tratamento de falha, quais são as suas etapas e quantas falhas são consideradas por vez?

- **Identificação da Falha:** Determinar o que falhou.
- **Análise da Causa Raiz:** Entender por que a falha ocorreu.
- **Correção:** Corrigir o problema para evitar recorrências.
- **Teste e Validação:** Testar o sistema ou componente corrigido.
- **Monitoramento:** Monitorar o sistema após a correção.

---

### 8) De exemplos de aplicações de sistemas tolerantes a falhas e explique a importância do uso nos mesmos.

- **Sistemas de Controle de Tráfego Aéreo:** Gerencia o tráfego aéreo e aeroportuário. A tolerância a falhas é vital para a segurança.
- **Sistemas de Suporte à Vida em Hospitais:** Equipamentos médicos como ventiladores e monitores cardíacos.
- **Veículos Autônomos:** Processam dados sensoriais para tomar decisões de direção seguras.

---

### 9) Encontre os bits de controle que serão adicionados às mensagens utilizando a técnica de bit de paridade ímpar em bloco.

- **m1:** 01101101 0
- **m2:** 10010010 0
- **m3:** 10111001 0
- **m4:** 00101110 1
- **m5:** 11010011 0
- **m6:** 10101101 0
- **m7:** 11111010 1
- **m8:** 01010110 1
        **01000101 0**

---

### 10) Crie uma questão sobre os assuntos estudados e apresente uma resposta descritiva.

**Question:** How do you build fault tolerance into a web application?

**Answer:** Building fault tolerance into a web application involves designing with redundancy, proactive monitoring, automated backups and failovers, and implementing self-repairing mechanisms. These strategies ensure a reliable user experience despite unexpected problems.
