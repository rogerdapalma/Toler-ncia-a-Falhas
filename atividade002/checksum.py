def calculate_checksum(message1, message2):
  # Converte em bits
  m1 = int(message1, 2)
  m2 = int(message2, 2)

  # Soma as mensagens e obtém o resultado em binário
  soma = bin(m1 + m2)[2:]

  # resultado da soma tenha 8 bits, adicionando zeros à esquerda se necessário
  soma = soma.zfill(8)

  # Inverte os bits do resultado da soma para obter o checksum
  checksum = ''.join('1' if bit == '0' else '0' for bit in soma)

  return checksum


def verificar_checksum(mensagem1, mensagem2, checksum_recebido):
  checksum_calculado = calculate_checksum(mensagem1, mensagem2)
  return checksum_calculado == checksum_recebido


# Exemplo de uso
mensagem1 = input("Digite a primeira mensagem de 8 bits: ")
mensagem2 = input("Digite a segunda mensagem de 8 bits: ")
checksum_recebido = input("Digite o checksum recebido: ")

if verificar_checksum(mensagem1, mensagem2, checksum_recebido):
  print("O checksum está correto.")
else:
  print("O checksum está incorreto.")
## M1: 10101011      M2: 01001010  Checksum Inv: 00001010
