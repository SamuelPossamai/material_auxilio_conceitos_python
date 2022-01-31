
class Classe:

    def __init__(self):
        self.valor = 2.5

    def __int__(self):
        return int(self.valor)

    def __float__(self):
        return float(self.valor)

a = Classe()

print(int(a))
print(float(a))
