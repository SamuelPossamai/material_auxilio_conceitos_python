
class Base:

    def __init__(self):
        print('Base.__init__')

class Derivada(Base):

    def __init__(self):
        super().__init__()

Derivada()
