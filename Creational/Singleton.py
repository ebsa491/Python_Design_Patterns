# First method for design with singleton

class Singleton:
    
    class __Singleton:
        
        def __init__(self):
            self.value = None

    instance = None

    def __new__(cls):
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton

        return Singleton.instance

    def __getattr__(self, attr):
        return getattr(self.instance, attr)

    def __setattr__(self, attr):
        return setattr(self.instance, attr)

# Second method

class Singleton2:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)

        return cls.instance

# Third method

class MetaSingleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super().__call__(*args, **kwargs)

        return cls.__instance[cls]

class Singleton3(metaclass = MetaSingleton):
    pass

if __name__ == '__main__':
    obj = Singleton()
    obj.value = 1
    obj2 = Singleton()
    obj2.value = 2

    print(obj.value)
    print(obj2.value)
