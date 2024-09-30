# Scrivere un programma che stampi per tutti i numeri da 0 a 100 se sono pari o dispari

for i in range(101):
    if i % 2 == 0:
        print(f'{i} è un numero pari')
    else:
        print(f'{i} è un numero dispari')
