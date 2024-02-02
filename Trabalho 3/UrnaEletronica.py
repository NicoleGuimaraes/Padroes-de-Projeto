#Exercicio 2 - Desenvolva um sistema de urna eletrônica e boletim de urna para uma eleição. O sistema deve permitir que os eleitores votem em candidatos e que os votos sejam contabilizados e exibidos em um boletim em tempo real



from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, candidato, numero_de_votos):
        pass

class Subject(ABC):
    @abstractmethod
    def adicionar(self, obj):
        pass

    @abstractmethod
    def remover(self, obj):
        pass

    @abstractmethod
    def notificar(self):
        pass

class Candidato(Subject):
    def __init__(self, nome):
        self.nome = nome
        self.numero_de_votos = 0
        self.lista_de_obj = []

    def adicionar(self, obj):
        self.lista_de_obj.append(obj)

    def remover(self, obj):
        self.lista_de_obj.remove(obj)

    def recebeu_voto(self):
        self.numero_de_votos += 1
        self.notificar()

    def notificar(self):
        for eachObj in self.lista_de_obj:
            eachObj.update(self.nome, self.numero_de_votos)

class Eleitor(Observer):
    def __init__(self, nome):
        self.nome = nome

    def votar(self, candidato):
        candidato.recebeu_voto()

    def update(self, candidato, numero_de_votos):
        print("Caro Eleitor " + self.nome + ", o candidato " + candidato + " recebeu " + str(numero_de_votos) + " votos")

class Boletim(Observer):
    def __init__(self, nome):
        self.nome = nome

    def update(self, candidato, numero_de_votos):
        print("Boletim de Urna: O candidato " + candidato + " recebeu " + str(numero_de_votos) + " votos")

if __name__ == '__main__':
    candidato1 = Candidato("Jacare")
    eleitor1 = Eleitor("Lucas")
    eleitor2 = Eleitor("Maria")
    boletim = Boletim("Boletim Principal")

    candidato1.adicionar(eleitor1)
    candidato1.adicionar(eleitor2)
    candidato1.adicionar(boletim)

    eleitor1.votar(candidato1)
    eleitor2.votar(candidato1)
