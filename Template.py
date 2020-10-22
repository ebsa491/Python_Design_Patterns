from abc import ABCMeta, abstractmethod

# Abstract class
class Compiler(metaclass=ABCMeta):

    @abstractmethod
    def get_source_code(self):
        pass

    @abstractmethod
    def compile_source(self):
        pass

    @abstractmethod
    def run(self):
        pass
    
    # Template method
    def compile_and_run(self):
        self.get_source_code()
        self.compile_source()
        self.run()

# Concrete class
class CPP(Compiler):

    def get_source_code(self):
        print("give me the source code (C++)... DONE")

    def compile_source(self):
        print("Compiling the source code (C++)... DONE")

    def run(self):
        print("Running the compiled object (C++)... DONE")

class Go(Compiler):

    def get_source_code(self):
        print("give me the source code (Go)... DONE")

    def compile_source(self):
        print("Compiling the source code (Go)... DONE")

    def run(self):
        print("Running the compiled object (Go)... DONE")

if __name__ == '__main__':
    cpp_compiler = CPP()
    cpp_compiler.compile_and_run()

    go_interpreter = Go()
    go_interpreter.compile_and_run()
