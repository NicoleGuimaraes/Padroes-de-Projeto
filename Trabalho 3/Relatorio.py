#seguindo o mesmo modelo do exercicio do café e do hamburguer usando o decorator

#Suponha que você esteja desenvolvendo um sistema de geração de relatórios contábeis para uma empresa. Este sistema deve ser capaz de gerar relatórios financeiros com diferentes níveis de detalhes e formatações (HTML, PDF, Relatorio Simples, Relatório Completo)


from abc import ABC, abstractmethod

class RelatorioFinanceiro(ABC): 
    @abstractmethod
    def gerar_relatorio(self):
        pass

class RelatorioSimples(RelatorioFinanceiro):
    def gerar_relatorio(self):
        print("Relatório Simples: Contas a pagar, Contas a receber")

class DecoratorRelatorio(RelatorioFinanceiro, ABC):
    def __init__(self, relatorio: RelatorioFinanceiro):
        self._relatorio = relatorio

class DecoratorRelatorioCompleto(DecoratorRelatorio):
    def gerar_relatorio(self):
        print("Relatório Completo: Balanço Patrimonial, Demonstrativo de Resultado")


class DecoratorFormatoHTML(DecoratorRelatorio):
    def gerar_relatorio(self):
      return f"<html>{self._relatorio.gerar_relatorio()}</html>"
      


class DecoratorFormatoPDF(DecoratorRelatorio):
    def gerar_relatorio(self):
        return f"PDF: {self._relatorio.gerar_relatorio()}"


if __name__ == '__main__':
    relatorio_simples = RelatorioSimples()

    relatorio_completo_html = DecoratorFormatoHTML(DecoratorRelatorioCompleto(relatorio_simples))
    relatorio_pdf = DecoratorFormatoPDF(relatorio_simples)

    print("Relatório Simples:")
    print(relatorio_simples.gerar_relatorio())
    print("\nRelatório Completo com Formato HTML:")
    print(relatorio_completo_html.gerar_relatorio())
    print("\nRelatório Simples com Formato PDF:")
    print(relatorio_pdf.gerar_relatorio())
