from abc import ABCMeta, abstractmethod

# Subject
class Pay(metaclass = ABCMeta):

    @abstractmethod
    def buy_it(self):
        pass

# Real Subject
class Bank(Pay):

    def buy_it(self):
        print("=== Bank buy ===")

# Proxy
class Card(Pay):

    def __init__(self):
        self.bank = Bank()

    def buy_it(self):
        self.bank.buy_it()
        print("==== Card buy ===")

# Client
class Client:
    def __init__(self):
        self.card = Card()
    
    def buy(self):
        self.card.buy_it()

if __name__ == '__main__':
    me = Client()
    me.buy()
