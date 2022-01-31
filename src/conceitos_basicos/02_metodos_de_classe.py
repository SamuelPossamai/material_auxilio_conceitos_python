
class Classe:

    atributo_da_classe = 'Texto'

    @classmethod
    def metodo_da_classe(cls):
        print(cls.atributo_da_classe)

a = Classe()

a.metodo_da_classe()
Classe.metodo_da_classe()
