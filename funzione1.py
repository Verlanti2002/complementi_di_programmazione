# Scrivere un programma che chieda all'utente di immettere una serie di valori terminata dal simbolo '#'
# Dopodichè applica una funzione a vostro piacere su tutti gli elementi
# Non usare un ciclo per l'applicazione della funzione

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
    except ValueError as e:
        print(f'Exception: {e}')

print(list(map(square, lista)))