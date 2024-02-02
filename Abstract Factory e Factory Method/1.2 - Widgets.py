from abc import ABC, abstractmethod

#interface abstrata para botões, menu e texto
class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class TextBox(ABC):
    @abstractmethod
    def input_text(self, text):
        pass

    @abstractmethod
    def get_text(self):
        pass


class Menu(ABC):
    @abstractmethod
    def select_option(self, option):
        pass

#factory abstrata para widgets
class WidgetFactory(ABC):
    @abstractmethod
    def criar_button(self) -> Button:
        pass

    @abstractmethod
    def criar_text_box(self) -> TextBox:
        pass

    @abstractmethod
    def criar_menu(self) -> Menu:
        pass

#implementações concretas de botões, texto e menus
class ModernoButton(Button):
    def click(self):
        print("Botão modernoo clicado.")

class ClassicoButton(Button):
    def click(self):
        print("Botão clássico clicado.")


class ModernoTextBox(TextBox):
    def input_text(self, text):
        print(f"Caixa de texto moderna recebeu: {text}")

    def get_text(self):
        return "Texto da caixa de texto modernoa"

class ClassicoTextBox(TextBox):
    def input_text(self, text):
        print(f"Caixa de texto clássica recebeu: {text}")

    def get_text(self):
        return "Texto da caixa de texto clássica"


class ModernoMenu(Menu):
    def select_option(self, option):
        print(f"Opção do menu moderno selecionada: {option}")

class ClassicoMenu(Menu):
    def select_option(self, option):
        print(f"Opção do menu clássico selecionada: {option}")

#factory concreta para estilo moderno e classico de GUI
class ModernoWidgetFactory(WidgetFactory):
    def criar_button(self) -> Button:
        return ModernoButton()

    def criar_text_box(self) -> TextBox:
        return ModernoTextBox()

    def criar_menu(self) -> Menu:
        return ModernoMenu()

class ClassicoWidgetFactory(WidgetFactory):
    def criar_button(self) -> Button:
        return ClassicoButton()

    def criar_text_box(self) -> TextBox:
        return ClassicoTextBox()

    def criar_menu(self) -> Menu:
        return ClassicoMenu()


def main():
    moderno_factory = ModernoWidgetFactory()
    classico_factory = ClassicoWidgetFactory()

    moderno_button = moderno_factory.criar_button()
    moderno_text_box = moderno_factory.criar_text_box()
    moderno_menu = moderno_factory.criar_menu()

    classico_button = classico_factory.criar_button()
    classico_text_box = classico_factory.criar_text_box()
    classico_menu = classico_factory.criar_menu()

    moderno_button.click()
    moderno_text_box.input_text("Bem vindo ao GUI Mordeno!")
    print(moderno_text_box.get_text())
    moderno_menu.select_option("opção 1")

    classico_button.click()
    classico_text_box.input_text("Bem vindo ao GUI Classicoo!")
    print(classico_text_box.get_text())
    classico_menu.select_option("opção A")

if __name__ == "__main__":
    main()
