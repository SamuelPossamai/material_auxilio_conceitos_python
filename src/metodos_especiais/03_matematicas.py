
import math

class Classe:

    def __init__(self):
        self.valor = 2.5

    def __add__(self, outro):
        print('__add__')
        return self.valor + outro

    def __radd__(self, outro):
        print('__radd__')
        return outro + self.valor

    def __mul__(self, outro):
        print('__mul__')
        return self.valor*outro

    def __rmul__(self, outro):
        print('__rmul__')
        return outro*self.valor

    def __truediv__(self, outro):
        print('__truediv__')
        return self.valor/outro

    def __rtruediv__(self, outro):
        print('__rtruediv__')
        return outro/self.valor

    def __floordiv__(self, outro):
        print('__floordiv__')
        return self.valor//outro

    def __rfloordiv__(self, outro):
        print('__rfloordiv__')
        return outro//self.valor

    def __mod__(self, outro):
        print('__mod__')
        return self.valor%outro

    def __rmod__(self, outro):
        print('__rmod__')
        return outro%self.valor

    def __divmod__(self, outro):
        print('__divmod__')
        return divmod(self.valor, outro)

    def __rdivmod__(self, outro):
        print('__rdivmod__')
        return divmod(outro, self.valor)

    def __sub__(self, outro):
        print('__sub__')
        return self.valor - outro

    def __rsub__(self, outro):
        print('__rsub__')
        return outro - self.valor

    def __pow__(self, outro):
        print('__pow__')
        return self.valor**outro

    def __rpow__(self, outro):
        print('__rpow__')
        return outro**self.valor

    def __abs__(self):
        print('__abs__')
        return abs(self.valor)

    def __round__(self):
        print('__round__')
        return round(self.valor)

    def __trunc__(self):
        print('__trunc__')
        return math.trunc(self.valor)

    def __floor__(self):
        print('__floor__')
        return math.floor(self.valor)

    def __ceil__(self):
        print('__ceil__')
        return math.ceil(self.valor)

a = Classe()

#print(dir(0))
a + 2
2 + a
a*2
2*a
a/2
2/a
a//2
2//a
a%2
2%a
divmod(a, 2)
divmod(2, a)
a - 2
2 - a
a**2
2**a
abs(a)
round(a)
math.trunc(a)
math.floor(a)
math.ceil(a)
