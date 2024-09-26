# Modificare il programma precedente in modo da non terminare finchè l'utente non inserisce il testo 'Fine'

while True:
    val = input('Inserire un valore: ')
    if val == '1':
        print('Red')
    elif val == '2':
        print('Blue')
    elif val == '3':
        print('Green')
    elif val == 'Fine':
        break
    else:
        print('Error')