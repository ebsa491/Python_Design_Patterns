# Facade

class Facade:

    def __init__(self):
        print("I'm the facade. Talk to me if you want something...")

    def start_subsystem_1(self):
        self.__subsystem_1 = Subsystem1()
        self.__subsystem_1.start()

    def start_subsystem_2(self):
        self.__subsystem_2 = Subsystem2()
        self.__subsystem_2.start()

    def start_subsystem_3(self):
        self.__subsystem_3 = Subsystem3()
        self.__subsystem_3.start()

# Subsystems

class Subsystem1:

    def __init__(self):
        print("Subsystem 1 is ready to start...")

    def start(self):
        print("Subsystem 1 started!")

class Subsystem2:

    def __init__(self):
        print("Subsystem 2 is ready to start...")

    def start(self):
        print("Subsystem 2 started!")

class Subsystem3:
    
    def __init__(self):
        print("Subsystem 3 is ready to start...")

    def start(self):
        print("Subsystem 3 started!")

# Client

class Client:
    
    def __init__(self):
        print("We should start the system but I don't know anything about it so I'll talk to the facade...")

    def talk_to_the_facade(self):
        self.facade = Facade()
        self.facade.start_subsystem_1()
        self.facade.start_subsystem_2()
        self.facade.start_subsystem_3()

if __name__ == '__main__':
    app = Client()
    app.talk_to_the_facade()