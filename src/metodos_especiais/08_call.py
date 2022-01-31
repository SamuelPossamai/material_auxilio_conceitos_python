
class Classe:

    def __init__(self, valor):
        self.valor = valor

    def __call__(self):
        return self.valor

a = Classe('Valor')

print(a())
