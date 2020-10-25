# First method

class Monostate:
    __shared_state = {'1': '2'}

    def __init__(self):
        self.__dict__ = self.__shared_state

# Second method

class Monostate2:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj

if __name__ == '__main__':

    # method 1

    obj1 = Monostate()
    obj1.x = 10
    obj2 = Monostate()
    obj2.x = 20

    print(obj1.x)
    print(obj2.x)

    # method 2

    obj1 = Monostate2()
    obj1.x = 10
    obj2 = Monostate2()
    obj2.x = 20

    print(obj1.x)
    print(obj2.x)