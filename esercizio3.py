# Scrivere un programma che prenda un valore inserito dall’utente
# Se è 1 stampa 'red'
# Se è 2 stampa 'blue'
# Se è 3 stampa 'green'
# Negli altri casi stampa un messaggio di errore

val = int(input('Inserire un valore: '))
if val == 1:
    print('Red')
elif val == 2:
    print('Blue')
elif val == 3:
    print('Green')
else:
    print('Error')
