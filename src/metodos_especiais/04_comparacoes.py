
class Classe:

    def __init__(self):
        self.valor = 2.5

    def __eq__(self, other):
        print('__eq__')
        return self.valor == other

    def __ne__(self, other):
        print('__ne__')
        return self.valor != other

    def __lt__(self, other):
        print('__lt__')
        return self.valor < other

    def __le__(self, other):
        print('__le__')
        return self.valor <= other

    def __gt__(self, other):
        print('__gt__')
        return self.valor > other

    def __ge__(self, other):
        print('__ge__')
        return self.valor >= other

    def __bool__(self):
        print('__bool__')
        return bool(self.valor)

a = Classe()

a == 2
2 == a
a != 2
2 != a
a <= 2
2 <= a
a >= 2
2 >= a
a < 2
2 < a
a > 2
2 > a
bool(a)
not a
if a:
    pass
