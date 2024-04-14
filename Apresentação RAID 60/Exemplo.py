import numpy as np

def xor_blocos(*blocos):
    """ Aplica XOR entre blocos de dados. """
    resultado = blocos[0]
    for bloco in blocos[1:]:
        resultado = np.bitwise_xor(resultado, bloco)
    return resultado

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

    tamanho_faixa = len(blocos_de_dados) // num_faixas
    grupos_raid = {}

    for i in range(num_faixas):
        inicio = i * tamanho_faixa
        fim = inicio + tamanho_faixa
        dados_grupo = blocos_de_dados[inicio:fim]
        paridade_p = xor_blocos(*dados_grupo)
        paridade_q = xor_blocos(*[bloco[::-1] for bloco in dados_grupo])  # Simulação simples de paridade Q
        grupos_raid[f'Grupo RAID 6 {i+1}'] = {'Dados': dados_grupo, 'Paridade P': paridade_p, 'Paridade Q': paridade_q}

    return grupos_raid

# Exemplo de uso
dados = [np.random.randint(0, 256, 10, dtype=np.uint8) for _ in range(4)]
raid60 = simular_raid60(dados)

for grupo, conteudos in raid60.items():
    print(grupo)
    for chave, valor in conteudos.items():
        print(f"{chave}: {valor}\n")
