from abc import ABC, abstractmethod
from datetime import datetime

#classe abstrata para eventos
class Evento(ABC):
    def __init__(self, timestamp=None):
        self.timestamp = timestamp or datetime.now()

    @abstractmethod
    def log(self):
        pass

#subclasse concreta para eventos do tipo Erro
class ErroEvento(Evento):
    def log(self):
        print(f"[{self.timestamp}] Erro: Ocorreu um erro.")

#subclasse concreta para eventos do tipo Aviso
class AvisoEvento(Evento):
    def log(self):
        print(f"[{self.timestamp}] Aviso: Atenção, algo pode estar errado.")

#subclasse concreta para eventos do tipo Informativo
class InfoEvento(Evento):
    def log(self):
        print(f"[{self.timestamp}] Informativo: Informações importantes.")

#interface do Factory Method
class EventoFactory(ABC):
    @abstractmethod
    def criar_evento(self) -> Evento:
        pass

#implementação concreta do Factory Method para eventos do tipo Erro
class ErroEventoFactory(EventoFactory):
    def criar_evento(self) -> Evento:
        return ErroEvento()

#implementação concreta para Aviso
class AvisoEventoFactory(EventoFactory):
    def criar_evento(self) -> Evento:
        return AvisoEvento()

#implementação concreta para eventos Informativo
class InfoEventoFactory(EventoFactory):
    def criar_evento(self) -> Evento:
        return InfoEvento()

#função para criar e logar eventos
def log_evento(factory: EventoFactory):
    evento = factory.criar_evento()
    evento.log()

#uso do Factory Method para criar e logar diferentes tipos de eventos
def main():
    erro_factory = ErroEventoFactory()
    aviso_factory = AvisoEventoFactory()
    info_factory = InfoEventoFactory()

    log_evento(erro_factory)
    log_evento(aviso_factory)
    log_evento(info_factory)

if __name__ == "__main__":
    main()
