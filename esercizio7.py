# Scrivere un programma che prenda in input un testo lungo e stampi la frequenza di ogni carattere (in ordine crescente)

occorrenze = {}
text = input('Inserire un testo lungo: ')

# Conta le occorrenze di ogni carattere
for char in text:
    if char in occorrenze:
        occorrenze[char] += 1
    else:
        occorrenze[char] = 1

# Ordina le occorrenze in base alla frequenza (ordine crescente)
occorrenze_ordinate = dict(sorted(occorrenze.items(), key=lambda item: item[1]))

# Stampa i risultati
for key, value in occorrenze_ordinate.items():
    print(f'{key}: {value}')
