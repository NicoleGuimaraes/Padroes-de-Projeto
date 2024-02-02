from abc import ABC, abstractmethod

#interface abstrata para a fundação parede e telhado da casa
class Fundacao(ABC):
    @abstractmethod
    def cria_fundacao(self):
        pass


class Parede(ABC):
    @abstractmethod
    def cria_parede(self):
        pass


class Telhado(ABC):
    @abstractmethod
    def cria_telhado(self):
        pass

#fabrica abstrata para diferentes partes da casa
class PartesDaCasaFactory(ABC):
    @abstractmethod
    def constroi_fundacao(self) -> Fundacao:
        pass

    @abstractmethod
    def constroi_parede(self) -> Parede:
        pass

    @abstractmethod
    def constroi_telhado(self) -> Telhado:
        pass

#implementações concretas para a fundação da casa
class FundacaoMordena(Fundacao):
    def cria_fundacao(self):
        print("Construindo uma fundação moderna.")

class ColonialFoundation(Fundacao):
    def cria_fundacao(self):
        print("Construindo uma fundação colonial.")


class ParedeMorderna(Parede):
    def cria_parede(self):
        print("Construindo paredes modernas.")

class ParedeColonial(Parede):
    def cria_parede(self):
        print("Construindo paredes coloniais.")


class TelhadoModerno(Telhado):
    def cria_telhado(self):
        print("Construindo um telhado moderno.")

class TelhadoColonial(Telhado):
    def cria_telhado(self):
        print("Construindo um telhado colonial.")

#fabrica concreta para estilo contemporâneo
class CasaComtemporaniaFactory(PartesDaCasaFactory):
    def constroi_fundacao(self) -> Fundacao:
        return FundacaoMordena()

    def constroi_parede(self) -> Parede:
        return ParedeMorderna()

    def constroi_telhado(self) -> Telhado:
        return TelhadoModerno()

#fabrica concreta para estilo colonial
class CasaColonialFactory(PartesDaCasaFactory):
    def constroi_fundacao(self) -> Fundacao:
        return ColonialFoundation()

    def constroi_parede(self) -> Parede:
        return ParedeColonial()

    def constroi_telhado(self) -> Telhado:
        return TelhadoColonial()


def main():
    comtemporania_factory = CasaComtemporaniaFactory()
    colonial_factory = CasaColonialFactory()


    fundacao1 = comtemporania_factory.constroi_fundacao()
    parede1 = comtemporania_factory.constroi_parede()
    telhado1 = comtemporania_factory.constroi_telhado()

    fundacao2 = colonial_factory.constroi_fundacao()
    parede2 = colonial_factory.constroi_parede()
    telhado2 = colonial_factory.constroi_telhado()

    fundacao1.cria_fundacao()
    parede1.cria_parede()
    telhado1.cria_telhado()

    fundacao2.cria_fundacao()
    parede2.cria_parede()
    telhado2.cria_telhado()

if __name__ == "__main__":
    main()
