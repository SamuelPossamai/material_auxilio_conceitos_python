
class Classe:

    def __init__(self):
        self.valor = 2.5

    def __int__(self):
        print('__int__')
        return int(self.valor)

    def __float__(self):
        print('__float__')
        return float(self.valor)

a = Classe()

print(int(a))
print(float(a))
