# Tolerância a Falhas

**Ciência da Computação**

## Aula 07
### Detecção e diagnóstico de falhas

### Tratamento de erros com exceções

**Santa Maria – RS 2024**

**Professor: André Flores dos Santos**

---

## Tolerar Falhas

- Sistemas de software são intrinsecamente complexos e esta complexidade ainda é agravada pelos novos requisitos impostos pelas aplicações modernas como confiabilidade, segurança e disponibilidade.

- Na medida em que se aumenta a complexidade dos sistemas e também o número de sistemas desenvolvidos, simultaneamente se torna imprescindível a utilização de uma abordagem organizada e estruturada de trabalho.

### Prevenção de Falhas vs. Tolerância a Falhas

- Existem duas técnicas complementares que podem ser adotadas: a prevenção de falhas e a tolerância a falhas.

- A técnica de prevenção de falhas se baseia na tentativa de prever e evitar as falhas. Entretanto, muitas vezes é impossível evitar uma falha, como por exemplo, falhas em componentes físicos deteriorados com o tempo.

- Desta forma, faz-se necessário o emprego de técnicas de tolerância a falhas que visam manter o sistema em pleno funcionamento mesmo na presença de falhas.

---

## Eventos Anormais

- Tratamento de exceções permite lidar com condições anormais de funcionamento de um programa, de forma a torná-lo mais robusto e seguro a falhas.

### Exemplos de condições anormais:

- Acesso a um índice de um vetor,
- Tentativa de uso de um objeto não inicializado,
- Falha na leitura/escrita em um arquivo,
- Falha na transferência de informações, etc.

- Uma forma para tratar as condições anormais é através do emprego de técnicas de tratamento de exceções. Após a identificação de uma falha, uma exceção é levantada indicando a presença de um erro no sistema.

---

## Tratando Exceções em Java

- Java é uma linguagem que faz forte uso do conceito de tratamento de exceções.

- Uma exceção é uma indicação de que um problema ocorreu durante a execução de um programa. Ao invés de deixar o programa terminar, é possível escrever um código para manipular a exceção e continuar a execução do programa.

### Tratamento de exceção

- Quando uma exceção ocorre, diz-se que o código lança (throw) uma exceção.
- É possível então tratar a exceção (catch) e, quando possível, recuperar para uma situação normal.
- Uma exceção pode não ser capturada.

### Bloco try e catch

- O programador pode criar um bloco try para códigos que podem gerar exceções.
- Todo bloco try deve ser seguido por zero ou mais blocos catch.
- Cada bloco catch especifica o tipo de exceção que pode capturar e contém o tratamento para esta exceção.

### Exemplo
```java
public class ExcecaoTeste {
    public static void main(String args[]) {
        int a[] = new int[4];
        try {
            a[0] = Integer.parseInt(args[0]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Voce deve informar um valor por parametro " + e);
        } catch (NumberFormatException n) {
            System.out.println("Voce deve informar um valor numerico " + n);
        }
    }
}

```

- O erro ocorre porque não está sendo passado nenhum argumento na linha de comando ao executar o programa. Nesse caso, quando o programa tenta acessar `args[0]` para converter em um inteiro usando `Integer.parseInt(args[0])`, ele lança uma exceção `ArrayIndexOutOfBoundsException` porque não há argumentos passados na linha de comando.

---

## Bloco finally

- Depois do último bloco catch, é possível adicionar um bloco finally.
- O bloco finally é sempre executado, independente da ocorrência ou não da exceção.
- É utilizado para a liberação de recursos ou valores padrões de saída, pois mesmo que o bloco falhe os recursos ou valores são liberados.
- Caso não existam blocos catch, é obrigatório ter um bloco finally.
- A única maneira do bloco finally não ser executado é se existe uma chamada a `System.exit()` dentro do código, o que causa o término do programa.

### Exemplo
```java
public class HelloWorld {
    public static void main (String[] args) {
        int i = 0;
        String ola[] = { "OLAH!", "HELLO!", "CIAO!" };
        while (i < 4) {
            try {
                System.out.println(ola[i]);
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Altera Index valor");
                i = -1;
            } catch (Exception e) {
                System.out.println("teste " + e.toString());
            } finally {
                System.out.println("Isto sempre serah impresso");
            }
            ++i;
        }
    }
}
```
- Iteração 3 (`i = 3`):
  - Acesso ao elemento `ola[3]`.
  - Nesta iteração, ocorre `ArrayIndexOutOfBoundsException` porque o array `ola` possui apenas 3 elementos (índices válidos são 0, 1 e 2).

---

## Métodos com Exceções
```java
public class UsandoExcecoes {
    public static void main(String args[]) {
        try {
            throwException();
        } catch (Exception e) {
            System.err.println("Exception handled in main");
        }
        doesNotThrowException();
    }

    public static void throwException() throws Exception {
        // Method implementation
    }

    public static void doesNotThrowException() {
        // Method implementation
    }
}

```
```java
public static void throwException() throws Exception {
    try {
        System.out.println("Method throwException");
        throw new Exception(); // generate exception
    } catch (Exception e) {
        System.err.println("Exception handled in method throwException");
    } finally {
        System.err.println("Finally executed in throwException");
    }
}

```
```java
public static void doesNotThrowException() {
    try {
        System.out.println("Method doesNotThrowException");
    } catch (Exception e) {
        System.err.println(e.toString());
    } finally {
        System.err.println("Finally executed in doesNotThrowException");
    }
    System.out.println("End of method doesNotThrowException");
}

```
- Na definição de método é possível listar as exceções que podem ser disparadas, utilizando a cláusula `throws`.

### Criando nossa própria Exceção

- É possível criar exceções próprias estendendo a classe `Exception`, em Java.
- Exemplo:
```java
public class MinhaExececao extends Exception{
    ...S
}
```
  - Para disparar uma exceção criada:
  - Para capturar exceções criadas utilizamos os blocos try-catch.

  ```java
  throw new MinhaExcecao();
  ```

### Exemplo
```java
public class DivisaoPorZero extends Exception {
    private String info;

    public DivisaoPorZero(String str) {
        info = str;
    }

    public String toString() {
        return info;
    }
}

```
```java
public class Fracao {
    private int num;
    private int den;

    public Fracao(int n, int d) {
        num = n;
        den = d;
    }

    public Fracao Divisao(Fracao f) throws DivisaoPorZero {
        if (f.den == 0) {
            throw new DivisaoPorZero("Na Classe Fracao... divisao por zero");
        }

        return new Fracao(num * f.den, den * f.num);
    }
}

```
```java
public class Excecao {
    public static void main(String args[]) {
        Fracao a, b, c;

        a = new Fracao(5, 3);
        b = new Fracao(2, 0);

        try {
            c = a.Divisao(b);
        } catch (DivisaoPorZero dz) {
            System.out.println("Erro " + dz);
        }
    }
}
```
---

## Referências Bibliográficas

- **SILBERSCHATZ, A.** Sistemas operacionais: conceitos e aplicações. Addison-Wesley, 2000.
- **TANENBAUM, Andrew S.; VAN STEEN, Maarten.** Distributed systems: principles and paradigms. New Jersey: Prentice Hall, 2002.
- **WEBER, T.** Tolerância a falhas: conceitos e exemplos. Disponível em: [Conceitos Dependabilidade](http://www.inf.ufrgs.br/~taisy/disciplinas/textos/ConceitosDependabilidade.PDF)
- **SANTOS, F, André.** Hardware Fault Tolerance Techniques. Disponível em: [hdl:10183/178392](http://hdl.handle.net/10183/178392)

**Agradecimentos:**
- Ao Prof. Guilherme C. Kurtz, Ana Paula Canal por ter cedido seus materiais que embasaram esta aula.

---

**Santa Maria – RS 2024**

**Email:** andre.flores@ufn.edu.br
