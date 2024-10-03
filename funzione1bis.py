# Modificare il programma precedente in modo che l'utente possa inserire solo numeri
# Gestire gli altri casi tramite eccezioni

def square(n):
    return n**2

lista = []
while True:
    try:
        val = input('Inserire un valore (# per terminare): ')
        if val != '#':
            lista.append(int(val))
        else:
            break
    except ValueError:
        print('ERRORE: input errato!')
        exit()

print(list(map(square, lista)))