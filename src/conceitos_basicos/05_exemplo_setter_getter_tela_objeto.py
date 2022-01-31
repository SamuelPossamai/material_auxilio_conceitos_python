
class Tela:

    def __init__(self):
        self._objetos = []

    def atualizar(self):
        print('Uma mudança foi feita, a tela precisa atualizar')

    def adicionaObjeto(self, objeto):
        self._objetos.append(objeto)
        objeto.adicionaListener(self.atualizar)

class Objeto:

    def __init__(self):
        self._x = 0
        self._y = 0
        self._listeners = []
        self._atualizando = False

    def adicionaListener(self, listener):
        self._listeners.append(listener)

    @property
    def position(self):
        return self._x, self._y

    @position.setter
    def position(self, valor):
        self._x, self._y = valor
        if not self._atualizando:
            self._atualizando = True
            for listener in self._listeners:
                listener()
            self._atualizando = False

    @position.deleter
    def position(self):
        print('Tentou deletar')

    def atualizar(self):
        print('Atualizado')

tela = Tela()
objeto = Objeto()

tela.adicionaObjeto(objeto)

objeto.position = 100, 200

print(objeto.position)
