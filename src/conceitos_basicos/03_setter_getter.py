
class Classe:

    def __init__(self):
        self.atributo = 'Valor inicial'

    def set_atributo(self, valor):
        self.atributo = valor
        self.atualizar()

    def get_atributo(self):
        return self.atributo

    def atualizar(self):
        print('Atualizado')

a = Classe()

a.set_atributo('Valor final')

print(a.get_atributo())
