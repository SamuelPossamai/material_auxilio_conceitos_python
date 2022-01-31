
class Base:

    def metodo1(self):
        print('Base.metodo1')

    def metodo2(self):
        print('Base.metodo2')

class Derivada(Base):

    def metodo1(self):
        print('Derivada.metodo1')

    def metodo3(self):
        print('Derivada.metodo3')

d = Derivada()

d.metodo1()
d.metodo2()
d.metodo3()
