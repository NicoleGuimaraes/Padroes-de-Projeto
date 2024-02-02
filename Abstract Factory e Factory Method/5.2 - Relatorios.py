from abc import ABC, abstractmethod

#Interface abstrata para relatórios
class Relatorio(ABC):
    @abstractmethod
    def generate(self):
        pass

#subclasse concreta para formato PDF
class PDFRelatorio(Relatorio):
    def generate(self):
        print("Gerando relatório em formato PDF.")

#subclasse concreta para formato CSV
class CSVRelatorio(Relatorio):
    def generate(self):
        print("Gerando relatório em formato CSV.")

#subclasse concreta para formato HTML
class HTMLRelatorio(Relatorio):
    def generate(self):
        print("Gerando relatório em formato HTML.")

#interface do Factory Method
class RelatorioFactory(ABC):
    @abstractmethod
    def criar_relatorio(self) -> Relatorio:
        pass

#Implementação concreta do Factory Method para relatórios em formato PDF
class PDFRelatorioFactory(RelatorioFactory):
    def criar_relatorio(self) -> Relatorio:
        return PDFRelatorio()

#implementação concreta para relatórios em formato CSV
class CSVRelatorioFactory(RelatorioFactory):
    def criar_relatorio(self) -> Relatorio:
        return CSVRelatorio()

#implementação concreta relatórios em formato HTML
class HTMLRelatorioFactory(RelatorioFactory):
    def criar_relatorio(self) -> Relatorio:
        return HTMLRelatorio()

#cria e gera relatórios usando o Factory Method
def gerar_relatorio(factory: RelatorioFactory):
    report = factory.criar_relatorio()
    report.generate()

#uso do Factory Method para criar e gerar diferentes tipos de relatórios
def main():
    pdf_factory = PDFRelatorioFactory()
    csv_factory = CSVRelatorioFactory()
    html_factory = HTMLRelatorioFactory()

    gerar_relatorio(pdf_factory)
    gerar_relatorio(csv_factory)
    gerar_relatorio(html_factory)

if __name__ == "__main__":
    main()
