# Aula 06: Blocos Básicos de Construção - Armazenamento Estável

## Informações do Professor
- **Nome**: André Flores dos Santos
- **Local**: Santa Maria – RS, 2024
- **Curso**: Ciência da Computação

## Armazenamento Estável
### Repositório Estável
- Técnicas de tolerância a falhas frequentemente requerem que parte do estado do sistema esteja disponível após uma falha.
- É suposto que o sistema possua um repositório estável, cujo conteúdo é preservado mesmo em caso de falhas.
- Discos comuns não são aceitáveis como repositório confiável devido às suas limitações.

### Características de um Repositório Estável
- Deve aumentar a confiabilidade tornando-se tolerante aos tipos de falhas mais comuns.
- É necessário entender o sistema físico (como discos) e seus modos de falha para construir um repositório estável.

### Exemplo de Operações em um Repositório Estável
- `write(addr, data)`: Escreve dados no endereço especificado.
- `read(addr) returns (status, data)`: Lê dados do endereço especificado, retornando o status e os dados.

### Tipos de Erros em Sistemas de Discos
- Falhas Transientes: Comportamento imprevisível de curta duração do disco.
- Bad Sector: Página corrompida cujos dados não podem ser lidos devido a falhas físicas.
- Falha da Controladora: Torna o conteúdo do disco inacessível mas não corrompido.
- Falha do Disco: Disco completamente ilegível devido a falha de hardware.

### Estratégias para Construir um Repositório Estável
- Mascarar eventos indesejados.
- Gerenciar erros não detectados e corrigir falhas persistentes.
- Utilizar redundância para proteger contra falhas físicas.

### Implementação de Armazenamento Estável com um Único Disco
- Particiona o disco em pares de páginas não relacionadas por deterioração.
- Implementa operações `StableRead` e `StableWrite` que lidam com falhas de forma redundante.

### Sombreamento de Disco (Disk Shadowing)
- Mantém cópias idênticas dos dados em discos separados para permitir acesso após falhas.
- O espelhamento de discos suporta defeitos por colapso e permite acesso contínuo durante reparos.

### RAID (Redundant Array of Independent Disks)
- **RAID 0**: Melhora a performance com striping, mas não oferece proteção contra falhas.
- **RAID 1**: Espelha completamente os dados para proporcionar alta disponibilidade.
- **RAID 2**: Usa códigos de Hamming para correção de erros, dividindo os dados em bits individuais.
- **RAID 3**: Utiliza striping com um disco dedicado a armazenar bits de paridade para recuperação de dados.

## Atividade
- Pesquisar e apresentar uma técnica RAID específica, abordando funcionamento, vantagens e desvantagens.

## Referências Bibliográficas
- SILBERSCHATZ, A. *Sistemas operacionais: conceitos e aplicações*. Addison-Wesley, 2000.
- TANENBAUM, Andrew S.; VAN Steen, Maarten. *Distributed systems: principles and paradigms*. New Jersey: Prentice Hall, 2002.
- WEBER, T. *Tolerância a falhas: conceitos e exemplos*. Disponível em [Link](http://www.inf.ufrgs.br/~taisy/disciplinas/textos/ConceitosDependabilidade.PDF).

## Agradecimentos
- Agradecimentos ao Prof. Guilherme C. Kurtz, Ana Paula Canal por seus materiais.
