
for i in range(20):

    if i % 2 != 0 or i % 3 != 0:
        continue

    print('for', i)

    if i >= 5:
        break

else:
    print('Chegou ao fim do loop sem usar \'break\'')
