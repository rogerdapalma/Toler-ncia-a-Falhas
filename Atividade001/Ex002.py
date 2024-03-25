#b) Falha de resposta
#Exercício desafio: Implemente um algoritmo em python para simular uma falha de resposta.

import random


def server():
  # chance de o servidor falhar
  probabilidade_erro = 0.3

  # verefica se o servidor falhou
  if random.random() < probabilidade_erro:
    print("Falha de resposta: Não foi possivel responder!")
  else:
    print("Sucesso! .")


# Exec
server()
