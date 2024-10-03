# Modificare il programma precedente utilizzando una lambda function

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

print(list(map(lambda n:n**2, lista)))