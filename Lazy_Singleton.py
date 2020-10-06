class Singleton:

    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("We're going to create the obj...")
        else:
            print("We created it before...", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

if __name__ == '__main__':
    s0 = Singleton()
    s1 = Singleton()
    print("obj created...", Singleton.get_instance())
    s2 = Singleton()
    s3 = Singleton()
