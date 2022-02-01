
def printar_pares(inicio=0, fim=10):

    if inicio % 2 == 1:
        inicio += 1

    for i in range(inicio, fim + 1, 2):
        print(i, end=' ')

    print()

printar_pares()
printar_pares(1)
printar_pares(1, 6)
printar_pares(1, fim=11)
printar_pares(inicio=1, fim=9)
