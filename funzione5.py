# Creare una funzione chiamata concatenate_strings che:
    # 1. accetta un numero variabile di stringhe come argomenti posizionali (*args)
    # 2. e una stringa separatore opzionale come keyword argument (separator)
# La funzione deve concatenare tutte le stringhe passate utilizzando il separatore indicato
# Esempio:
# $- concatenate_strings('Hello', 'World', separator='-')
# $- "Hello-World"

from  functools  import  reduce

def concatenate_strings(*args, separator):
    return reduce(lambda x, y: x+separator+y, *args)

lista = []
while True:
    stringa = input('Inserire una stringa (# per terminare): ')
    if stringa != '#':
        lista.append(stringa)
    else:
        break

if input('Vuole inserire anche un elemento separatore? ') == 'si':
    separatore = input("Inserire l'elemento separatore: ")
    print(concatenate_strings(lista, separator=separatore))
else:
    print(concatenate_strings(lista, separator='-')) # separatore di default