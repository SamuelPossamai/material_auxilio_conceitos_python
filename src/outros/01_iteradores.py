
a = (1, 2)
b = 1, 2

print(a == b, type(a))

c, d = a

print(c, d)

iterador = iter(a)

print(next(iterador))
print(next(iterador))
#print(next(iterador))

iterador = iter(a)

for i in iterador:
    print(i)
