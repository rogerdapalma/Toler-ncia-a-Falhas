import numpy as np  # Importa a biblioteca numpy

def xor_blocos(*blocos):
    """ Aplica XOR entre blocos de dados. """
    resultado = blocos[0]  # Inicializa o resultado com o primeiro bloco
    for bloco in blocos[1:]:  # Itera sobre os blocos restantes
        resultado = np.bitwise_xor(resultado, bloco)  # Aplica XOR entre o resultado atual e o próximo bloco
    return resultado  # Retorna o resultado final do XOR

def simular_raid60(blocos_de_dados, num_faixas=2):
    """
    Simula RAID 60 com dupla paridade e distribuição entre grupos RAID 6.

    Args:
    blocos_de_dados (lista de np.array): Blocos de dados para armazenar.
    num_faixas (int): Número de subgrupos RAID 6.

    Returns:
    dict: Um dicionário contendo os dados e paridades.
    """
    if len(blocos_de_dados) % num_faixas != 0:
        raise ValueError("O número de blocos de dados deve ser múltiplo do número de subgrupos RAID 6.")

    tamanho_faixa = len(blocos_de_dados) // num_faixas  # Calcula o número de blocos por faixa
    grupos_raid = {}  # Dicionário para armazenar os grupos de RAID 6

    for i in range(num_faixas):
        inicio = i * tamanho_faixa  # Índice inicial da faixa
        fim = inicio + tamanho_faixa  # Índice final da faixa
        dados_grupo = blocos_de_dados[inicio:fim]  # Seleciona os dados da faixa atual
        paridade_p = xor_blocos(*dados_grupo)  # Calcula a paridade P usando XOR dos blocos
        paridade_q = xor_blocos(*[bloco[::-1] for bloco in dados_grupo])  # Calcula a paridade Q (XOR dos blocos invertidos)
        grupos_raid[f'Grupo RAID 6 {i+1}'] = {'Dados': dados_grupo, 'Paridade P': paridade_p, 'Paridade Q': paridade_q}

    return grupos_raid  # Retorna o dicionário com dados e paridades dos grupos RAID 6

# Exemplo de uso
dados = [np.random.randint(0, 256, 10, dtype=np.uint8) for _ in range(4)]  # Gera dados aleatórios
raid60 = simular_raid60(dados)  # Simula RAID 60 com os dados

for grupo, conteudos in raid60.items():  # Itera sobre os grupos de RAID 60
    print(grupo)
    for chave, valor in conteudos.items():  # Itera sobre os dados e paridades de cada grupo
        print(f"{chave}: {valor}\n")  # Imprime as informações
