#Utilizando decorator e baseando no exemplo do exercicio do café
#Desenvolva um sistema para o McDonalds que permita que os clientes crie hambúrgueres com ingredientes personalizados 



from abc import ABC, abstractmethod

class Hamburguer(ABC):
    @abstractmethod
    def preparar(self) -> str:
        pass


class HamburguerSimples(Hamburguer):
    def preparar(self) -> str:
        return "Hambúrguer simples"


class HamburguerDecorator(Hamburguer, ABC):
    def __init__(self, hamburguer: Hamburguer):
        self._hamburguer = hamburguer

    @abstractmethod
    def preparar(self) -> str:
        pass


class QueijoDecorator(HamburguerDecorator):
    def preparar(self) -> str:
        return f"{self._hamburguer.preparar()}, com queijo"


class TomateDecorator(HamburguerDecorator):
    def preparar(self) -> str:
        return f"{self._hamburguer.preparar()}, com tomate"


class BaconDecorator(HamburguerDecorator):
    def preparar(self) -> str:
        return f"{self._hamburguer.preparar()}, com bacon"


class AlfaceDecorator(HamburguerDecorator):
    def preparar(self) -> str:
        return f"{self._hamburguer.preparar()}, com alface"


basico_hamburguer = HamburguerSimples()
hamburguer_com_queijo_bacon = BaconDecorator(QueijoDecorator(basico_hamburguer))
hamburguer_com_alface_tomate_bacon = BaconDecorator(AlfaceDecorator(TomateDecorator(basico_hamburguer)))


print("Hambúrguer básico:", basico_hamburguer.preparar())
print("Hambúrguer com queijo e bacon:", hamburguer_com_queijo_bacon.preparar())
print("Hambúrguer com tomate, alface e bacon:", hamburguer_com_alface_tomate_bacon.preparar())
