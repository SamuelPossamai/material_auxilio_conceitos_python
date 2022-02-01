
class Class(object):

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')

with Class() as c:
    print(c)
    #raise Exception
