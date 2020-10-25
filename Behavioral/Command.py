from abc import ABCMeta, abstractmethod

# Command
class Command(metaclass = ABCMeta):

    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass

# Concrete Command
class ConcreteCommand(Command):

    def execute(self):
        self.receiver.run()

# Receiver
class Receiver:

    def run(self):
        print("Running")

# Invoker
class Invoker:

    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()

# Client

if __name__ == '__main__':
    receive = Receiver()
    cmd = ConcreteCommand(receive)
    invok = Invoker()
    invok.command(cmd)
    invok.execute()
