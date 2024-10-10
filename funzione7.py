# Utilizzare un'espressione generatrice per creare un generatore che produca tutti i numeri dispari tra 0 e un numero n fornito dall'utente
# Utilizzare il generatore per stampare uno a uno tutti i numeri dispari generati

n = int(input('Inserire un numero: '))
for x in (x for x in range(n+1) if x % 2 != 0):
    print(x)