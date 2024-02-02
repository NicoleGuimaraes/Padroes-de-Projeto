from abc import ABC, abstractmethod

#classe abstrata para documentos
class Doc(ABC):
    @abstractmethod
    def carregando(self):
        pass

#subclasse concreta para documentos PDF
class PDFDoc(Doc):
    def carregando(self):
        print("Carregando documento PDF.")

#subclasse concreta para documentos Word
class WordDoc(Doc):
    def carregando(self):
        print("Carregando documento Word.")

#subclasse concreta para documentos HTML
class HTMLDoc(Doc):
    def carregando(self):
        print("Carregando documento HTML.")

#interface do Factory Method
class DocFactory(ABC):
    @abstractmethod
    def criar_doc(self) -> Doc:
        pass

#implementação concreta para PDF
class PDFDocFactory(DocFactory):
    def criar_doc(self) -> Doc:
        return PDFDoc()

#implementação concreta para Word
class WordDocFactory(DocFactory):
    def criar_doc(self) -> Doc:
        return WordDoc()

#implementação concreta para HTML
class HTMLDocFactory(DocFactory):
    def criar_doc(self) -> Doc:
        return HTMLDoc()

#função para carregar um documento usando o Factory Method
def carregar_doc(factory: DocFactory):
    doc = factory.criar_doc()
    doc.carregando()

#uso do Factory Method para carregar diferentes tipos de documentos
def main():
    pdf_factory = PDFDocFactory()
    word_factory = WordDocFactory()
    html_factory = HTMLDocFactory()

    carregar_doc(pdf_factory)
    carregar_doc(word_factory)
    carregar_doc(html_factory)

if __name__ == "__main__":
    main()
