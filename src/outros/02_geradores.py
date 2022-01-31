
def gerador(inicio, fim):

    for i in range(inicio, fim):
        yield i**2

for squared in gerador(10, 20):
    print(squared)
