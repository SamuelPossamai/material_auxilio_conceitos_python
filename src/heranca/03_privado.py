
class Base:

    def __init__(self):
        self.__privado = 2

class Derivada(Base):

    def __init__(self):
        super().__init__()

        print(self.__privado)

Derivada()
