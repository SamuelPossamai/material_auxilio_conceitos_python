
class Classe:

    def __init__(self):
        self._atributo = 'Valor inicial'

    @property
    def atributo(self):
        return self._atributo

    @atributo.setter
    def atributo(self, valor):
        self._atributo = valor
        self.atualizar()

    @atributo.deleter
    def atributo(self):
        print('Tentou deletar')

    def atualizar(self):
        print('Atualizado')

a = Classe()

a.atributo = 'Valor final'

print(a.atributo)

del a.atributo
