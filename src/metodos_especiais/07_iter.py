
class Iterador:

    def __init__(self, inicio, fim):

        self.inicio = inicio
        self.atual = inicio
        self.fim = fim
        self.passo = 1

    def __iter__(self):
        return self

    def __next__(self):

        atual = self.atual

        if atual >= self.fim:
            raise StopIteration

        self.atual += self.passo

        return atual

for i in Iterador(10, 20):
    print(i, end=' ')

print()
