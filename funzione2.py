# Creare una lista di numeri e utilizzare una funzione anonima ("lambda") insieme a "filter" per ottenere una nuova lista contenente solo i numeri pari
# Stampare la lista risultante
# Successivamente, utilizzare la funzione "map" per ottenere una lista di quadrati dei numeri pari filtrati

lista = []
lista_risultante = []

while True:
    try:
        n = input('Inserire un valore (# per terminare): ')
        if n != '#':
            lista.append(int(n))
        else:
            break
    except ValueError as e:
        print(f'Exception: {e}')

lista_risultante = list(filter(lambda n:n%2==0, lista))
print(lista_risultante)
print(list(map(lambda n:n**2, lista_risultante)))    