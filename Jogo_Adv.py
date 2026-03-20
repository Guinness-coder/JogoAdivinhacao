from enum import nonmember
import random
from abc import ABC, abstractmethod

class Jogo(ABC):

  @abstractmethod
  def iniciar(self):
    pass

  @abstractmethod
  def jogar(self):
    pass

class Jogador:
  def __init__(self):
    self.nome = input("Nome do Jogador: ")
    self.pontos = 100

class Ranking:
  def __init__(self):
    self.jogadores = []

  def add_jogadores(self, jogador):
    self.jogadores.append(jogador)

  def exibir_ranking(self):
    self.jogadores.sort(key = lambda x: x.pontos, reverse = True)
    print("Ranking: ")
    for i, jogador in enumerate(self.jogadores):
      print(f" {i+1}. {jogador.nome}: {jogador.pontos} pontos")

class JogoAdivinhação(Jogo):

  def __init__(self, jogador: Jogador):
    self.jogador = jogador
    self._numero_secreto = random.randint(1,100)
    self._tentativas = 0
    self._limite = 10

  def iniciar(self):
    print("JOGO DA ADIVINHAÇÃO")
    print("Pontuação atual: ", self.jogador.pontos)
    print("Tente adivinhar o número entre 1 e 100")
    print("Você tem", self._limite, "tentativas")

  def jogar(self):

    while self._tentativas < self._limite:

      try:
        palpite = int(input("Digite seu palpite: "))
      except:
        print("Digite apenas números!")
        continue

      self._tentativas += 1

      if palpite == self._numero_secreto:
        print("Parabéns! Você acertou!")
        self.jogador.pontos += 10
        print("Pontuação final:", self.jogador.pontos)
        print("Tentativas usadas:", self._tentativas)
        return

      elif palpite < self._numero_secreto:
        print("O número secreto é MAIOR")
        self.jogador.pontos -= 2
        print("Pontuação atual: ", self.jogador.pontos)
      else:
        print("O número secreto é MENOR")
        self.jogador.pontos -= 2
        print("Pontuação atual: ", self.jogador.pontos)

    print("Suas tentativas acabaram!")
    print("O número secreto era: ", self._numero_secreto)

def executar_jogo(jogo: Jogo):
  jogo.iniciar()
  jogo.jogar()

ranking_instance = Ranking()
jogador_instance = Jogador()
jogo = JogoAdivinhação(jogador_instance)
executar_jogo(jogo)

ranking_instance.add_jogadores(jogador_instance)
ranking_instance.exibir_ranking()
