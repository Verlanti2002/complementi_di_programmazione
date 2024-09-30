# Scrivere un programma che prenda in input un testo lungo e stampi la frequenza di ogni carattere (in ordine crescente)

occorrenze = []
i = 0
y = 0
text = input('Inserire un testo lungo: ')

for i in text:
    c = 0
    for y in text:
        if text[i] == text[y]:
            c = c + 1
    occorrenze[i] = c

occorrenze.sort()

for i in text:
    print(f'{i}: {occorrenze[i]}')
