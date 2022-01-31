
class Classe:

    def metodo(self):
        print('Método')

a = Classe()

a.metodo()
Classe.metodo(a)

print(a.metodo)
print(Classe.metodo)
