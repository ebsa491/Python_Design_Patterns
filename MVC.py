class Model:
    def __init__(self):
        self.__data = [1, 2, 3, 4]

    def get_data(self):
        return self.__data

class View:
    def print_data(self, data):
        for a in data:
            print(a)

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def handle_data(self):
        self.view.print_data(self.model.get_data())

class Client:
    def __init__(self):
        self.controller = Controller()
        self.controller.handle_data()

if __name__ == '__main__':
    app = Client()
