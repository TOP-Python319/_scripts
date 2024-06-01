class Computer:

    class CPU:
        def __init__(self):
            self.speed = "3.4 GHz"

    class Memory:
        def __init__(self):
            self.size = "16 GB"

    def __init__(self):
        self.cpu = self.__class__.CPU()
        self.memory = self.__class__.Memory()


computer = Computer()
