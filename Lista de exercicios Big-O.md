## Lista de Exercícios: Análise de Complexidade (Big-O)

### Definições das Funções
- **f(n) = 3n³ + 2n²**
- **g(n) = 2n² + 4n**
- **h(n) = 3n² + 5**
- **i(n) = 4n⁵ + 2n³**
- **j(n) = 3n² + 4n⁴**

### 1. **Cálculo de Notação Big-O para Cada Função**

- **f(n)**: O termo dominante é **3n³**.
  - `Notação Big-O: O(n³)`

- **g(n)**: O termo dominante é **2n²**.
  - `Notação Big-O: O(n²)`

- **h(n)**: O termo dominante é **3n²**.
  - `Notação Big-O: O(n²)`

- **i(n)**: O termo dominante é **4n⁵**.
  - `Notação Big-O: O(n⁵)`

- **j(n)**: O termo dominante é **4n⁴**.
  - `Notação Big-O: O(n⁴)`

### 2. **Verificação de Proposições**

- **a) O(F(N)) + O(O(F(N))) = o(F(N))** - **FALSA**
  - `O(n³) + O(n³) não é menor que O(n³).`

- **b) O(G(N)) + O(H(N)) = O(G(N))** - **FALSA**
  - `O(n²) + O(n²) é O(n²), mas não é igual a O(g(n)) ou O(h(n)) isoladamente.`

- **c) O(F(N)) * O(G(N)) = O(I(N))** - **VERDADEIRA**
  - `O(n³) * O(n²) = O(n⁵), que corresponde a O(i(n)).`

- **d) K * O(I(N)) * O(J(N)) = O(F(N)) * O(F(N)) * O(T(N))** - **DEPENDE DE T(N)**
  - `Se T(n) é tal que a expressão se equilibra, poderia ser verdadeira. Caso contrário, não é possível afirmar sem conhecer T(n).`

### 3. **Cálculo Combinado de Complexidades**

- **O(F(N)) + O(G(N)) + O(H(N)) + O(I(N)) + O(J(N))**
  - `A soma dessas complexidades é dominada pelo termo de maior ordem, O(n⁵), devido a i(n).`

- **O(F(N)) * O(G(N)) * O(H(N)) * O(I(N)) * O(J(N))**
  - `A multiplicação resulta em O(n³) * O(n²) * O(n²) * O(n⁵) * O(n⁵) = O(n¹⁷).`
