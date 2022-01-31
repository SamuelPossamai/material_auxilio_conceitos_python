
def decorador(func):

    def funcao_final():
        print(2*func())

    return funcao_final

@decorador
def funcao_decorada():
    return 2

def funcao_decorada_v2():
    return 2

funcao_decorada_v2 = decorador(funcao_decorada_v2)

funcao_decorada()
funcao_decorada_v2()
