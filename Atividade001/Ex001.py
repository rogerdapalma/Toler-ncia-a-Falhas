#a) Falha por temporização (timing)
#Exercício desafio:
#Implemente um algoritmo em python para simular uma falha por temporização.
#- Dicas para resolver o exercício:
#Utilize a biblioteca time: A biblioteca time em Python oferece funções para trabalhar com tempo. Você pode usar a função time.sleep (delay) para introduzir um atraso na resposta do servidor e causar algum problema, por exemplo, no envio ou recebimento da mensagem.

import time
import random


def server():
  #tempo maximo para responder
  tempo_max_resp = 5

  #tempo de processamento é aleatorio de 1 a 10
  #tempo_process = 7 ; forçando o tempo de processamento a atrasar
  tempo_process = random.randint(1, 10)
  print(f"Tempo de processamento do servidor: {tempo_process} segundos")

  #atraso no tempo_process
  time.sleep(tempo_process)

  # Verifica se houve uma falha por temporização
  if tempo_process > tempo_max_resp:
    print("Falha por temporização: foi exedido o tempo maximo do serivdor.")
  else:
    print("Resposta aceita! mensagem recebida com suceso.")


# Exec
server()
