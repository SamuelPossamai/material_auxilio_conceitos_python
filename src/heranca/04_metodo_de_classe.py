
class Base:

    NOME = 'Base'

    @classmethod
    def metodo(cls):
        print(cls.NOME)

class Derivada(Base):

    NOME = 'Derivada'

Derivada.metodo()
