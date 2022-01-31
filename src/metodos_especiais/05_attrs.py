
class Classe:

    def __init__(self):
        self._atributos = {
            'valor': 2.5
        }

    def __getattr__(self, name):
        print('__getattr__', name)
        return self._atributos[name]

    def __setattr__(self, name, valor):
        if name == '_atributos':
            self.__dict__['_atributos'] = valor
            return
        print('__setattr__', name)
        self._atributos[name] = valor

    def __delattr__(self, name):
        print('__delattr__', name)
        del self._atributos[name]

a = Classe()

a.valor = 5
print(a.valor)
del a.valor
