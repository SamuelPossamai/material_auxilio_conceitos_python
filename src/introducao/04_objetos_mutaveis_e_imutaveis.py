
# objetos imutaveis e mutaveis

def foo(a=[]):
    a.append(len(a))
    print(a)

foo()
foo()
foo()
foo()
