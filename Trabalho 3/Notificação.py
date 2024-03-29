#Suponha que você esteja desenvolvendo um sistema de notificação de preços para uma loja online. O sistema deve notificar os clientes sempre que o preço de um produto que está interessado for alterado. Utilize o padrão Observer para implementar esse sistema. 

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, nome_produto, valor):
        pass


class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Produto(Subject):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def unsubscribe(self, observer):
        self.subscribers.remove(observer)

    def notify(self):
        for observer in self.subscribers:
            observer.update(self.nome, self.preco)

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco
        self.notify()


class Loja:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def alterar_preco_produto(self, produto, novo_preco):
        produto.alterar_preco(novo_preco)


class Cliente(Observer):
    def __init__(self, nome):
        self.nome = nome

    def update(self, nome_produto, valor):
        print(self.nome + ', o valor de ' + nome_produto + ' foi atualizado para ' + valor)


if __name__ == '__main__':
    my_magic_loja = Loja()

    prod1 = Produto('Camiseta', 'R$20,00')
    prod2 = Produto('Calça', 'R$50,00')
    prod3 = Produto('Tênis', 'R$80,00')

    cli1 = Cliente('João')
    cli2 = Cliente('Maria')
    cli3 = Cliente('Pedro')

    my_magic_loja.adicionar_produto(prod1)
    my_magic_loja.adicionar_produto(prod2)
    my_magic_loja.adicionar_produto(prod3)
    
    prod1.subscribe(cli1)
    prod1.subscribe(cli2)
    prod2.subscribe(cli3)
    prod3.subscribe(cli2)

    print('valor da camisa atual: ' + prod1.preco)
    print('valor da calça atual: ' + prod2.preco)
  
    my_magic_loja.alterar_preco_produto(prod1, 'R$25,00')
    my_magic_loja.alterar_preco_produto(prod2, 'R$45,00')
