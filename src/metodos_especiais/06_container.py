
class Classe:

    def __init__(self):
        self._list = [1, 2, 3, 4, 5]

    def __getitem__(self, key):
        print('__getitem__', key)
        return self._list[key]

    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self._list[key] = value

    def __delitem__(self, key):
        print('__delitem__', key)
        del self._list[key]

    def __len__(self):
        print('__len__')
        return len(self._list)

    def __contains__(self, key):
        print('__contains__', key)
        return key in self._list

    def __reversed__(self):
        print('__reversed__')
        return reversed(self._list)

    def __iter__(self):
        print('__iter__')
        return iter(self._list)

a = Classe()

a[0]
a[1:2:3]
a[0] = 2
del a[0]
len(a)
2 in a
reversed(a)
for item in a:
    pass


