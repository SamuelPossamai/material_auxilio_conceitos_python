
class Classe:

    def __init__(self):
        self.__privado = 'Privado'

    def metodo(self):
        return self.__privado

a = Classe()

#print(a.__privado)
print(a._Classe__privado)
print(a.metodo())
