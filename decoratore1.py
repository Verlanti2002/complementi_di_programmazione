# Piccolo esempio di utilizzo dei decoratori di funzione

def d_f(f):
    def function(*args, **kwargs):
        print('Ciao!')
        return f(*args, **kwargs)
    return function

@d_f
def pippo(x, y, z):
    print(x)
    print(y)
    print(z)

# d_f(pippo)(1, 2, 3)
pippo(1,2,3)