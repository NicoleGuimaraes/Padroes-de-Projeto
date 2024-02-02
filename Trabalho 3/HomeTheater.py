#Suponha que você deseja construir seu proprio home theater. O sistema contém uma TV, um som surround, aparelhagem de DVD e um sintonizador para TV a cabo ou canais abertos. A TV tem as opções de ligar, desligar, controle de volume e escolha da entrada do sinal (DVD ou Sintonizador de TV). O Sistema de som surround tem as opções de Entrada (DVD ou Sintonizador de TV), controle de volume. Ligar estereo ou mono. O sintonizador de TV tem as opções de canais (AR ou Cabo) e opçoes de liga e desliga. Você deseja que o controle do seu sistema home theater seja feito de maneira automatizada por meio de um controle remoto. 

class TV:
  def __init__(self):
      self.ligada = False
      self.volume = 50

  def liga(self):
      self.ligada = True

  def desliga(self):
      self.ligada = False

  def aumenta_volume(self):
      self.volume += 10


class DVD:
  def __init__(self):
      self.ligado = False

  def liga(self):
      self.ligado = True

  def desliga(self):
      self.ligado = False

  def play(self):
      self.tv.liga()
      self.som.liga()
      self.tv.aumenta_volume()

class Som:
  def __init__(self):
      self.ligado = False
      self.volume = 50

  def liga(self):
      self.ligado = True

  def desliga(self):
      self.ligado = False

  def aumenta_volume(self):
      self.volume += 10



class Sintonizador:
  def __init__(self):
      self.ligado = False
      self.canal = "AR"

  def liga(self):
      self.ligado = True

  def desliga(self):
      self.ligado = False

  def inserir_canal(self, canal):
      if self.ligado:
          self.canal = canal


class HomeTheaterFacade:
  def __init__(self, tv, dvd, som, sintonizador):
      self.tv = tv
      self.dvd = dvd
      self.som = som
      self.sintonizador = sintonizador

  def escolher_entrada(self, entrada):
      if entrada == "DVD":
          self.dvd.liga()
          self.sintonizador.desliga()
      elif entrada == "Sintonizador":
          self.dvd.desliga()
          self.sintonizador.liga()


  def assistir_tv(self):
      self.tv.liga()
      self.sintonizador.liga()
      self.som.liga()
      self.tv.aumenta_volume()


if __name__ == "__main__":
  minha_tv = TV()
  meu_dvd = DVD()
  meu_som = Som()
  meu_sintonizador = Sintonizador()

  meu_home_theater = HomeTheaterFacade(minha_tv, meu_dvd, meu_som, meu_sintonizador)

  meu_home_theater.escolher_entrada("DVD")

  meu_home_theater.escolher_entrada("Sintonizador")
  meu_home_theater.assistir_tv()
