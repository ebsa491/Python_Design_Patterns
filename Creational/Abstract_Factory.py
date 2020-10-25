from abc import ABCMeta, abstractmethod

# Abstract Factory

class CoffeeFactory(metaclass = ABCMeta):

    @abstractmethod
    def serve_coffee_with_milk(self):
        pass

    @abstractmethod
    def serve_coffee_without_milk(self):
        pass

# Concrete Factories

class FrenchCoffeeFactory(CoffeeFactory):

    def serve_coffee_with_milk(self):
        return FrenchCappucino().serve(FrenchEspresso())

    def serve_coffee_without_milk(self):
        return FrenchEspresso().serve()

class ItalianCoffeeFactory(CoffeeFactory):

    def serve_coffee_with_milk(self):
        return ItalianCappucino().serve(ItalianEspresso())

    def serve_coffee_without_milk(self):
        return ItalianEspresso().serve()

# Abstract Products

class CoffeeWithMilk(metaclass = ABCMeta):

    @abstractmethod
    def serve(self, coffee_without_milk):
        pass

class CoffeeWithoutMilk(metaclass = ABCMeta):

    @abstractmethod
    def serve(self):
        pass

# Concrete Products

class FrenchCappucino(CoffeeWithMilk):

    def serve(self, coffee_without_milk):
        return f"French cappucino served from {str(coffee_without_milk)}."

class FrenchEspresso(CoffeeWithoutMilk):

    def serve(self):
        return f"French espresso served."

class ItalianCappucino(CoffeeWithMilk):

    def serve(self, coffee_without_milk):
        return f"Italian cappucino served from {str(coffee_without_milk)}."

class ItalianEspresso(CoffeeWithoutMilk):

    def serve(self):
        return f"Italian espresso served from."

# Client

class CoffeeStore:

    def __init__(self):
        self.french_factory = FrenchCoffeeFactory()
        self.italian_factory = ItalianCoffeeFactory()

    def serve_french_cappucino(self):
        return self.french_factory.serve_coffee_with_milk()

    def serve_french_espresso(self):
        return self.french_factory.serve_coffee_without_milk()

    def serve_italian_cappucino(self):
        return self.italian_factory.serve_coffee_with_milk()

    def serve_italian_espresso(self):
        return self.italian_factory.serve_coffee_without_milk()

if __name__ == '__main__':
    store = CoffeeStore()
    print(store.serve_french_cappucino())
    print(store.serve_french_espresso())
    print(store.serve_italian_cappucino())
    print(store.serve_italian_espresso())
