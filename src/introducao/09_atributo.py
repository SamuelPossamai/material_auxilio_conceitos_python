
class Classe:

    def __init__(self, attr):
        self.atributo = attr

    def metodo(self):
        self.atributo += 1
        print(self.atributo)

a = Classe(0)

a.metodo()
a.metodo()
