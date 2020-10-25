from abc import ABCMeta, abstractmethod

class State(metaclass = ABCMeta):

    @abstractmethod
    def handle(self):
        pass

class ConcreteState1(State):
    
    def handle(self):
        print("1")

class ConcreteState2(State):

    def handle(self):
        print("2")

class Context(State):

    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def handle(self):
        self.state.handle()

if __name__ == '__main__':
    cont = Context()
    state_1 = ConcreteState1()
    state_2 = ConcreteState2()

    cont.set_state(state_1)
    cont.handle()
    cont.set_state(state_2)
    cont.handle()
