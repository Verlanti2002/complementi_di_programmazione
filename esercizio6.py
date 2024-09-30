# Scrivere un programma che simuli una rubrica telefonica
# L'utente deve poter scegliere se inserire un numero, cancellarlo o stampare l'intera rubrica
# La struttura della rubrica è molto semplice ogni contatto ha un nome e un numero

rubrica = {} # {key='nome', value='telefono'}

while True:
    print('1 Aggiungere contatto')
    print('2 Cancellare un contatto')
    print('3 Stampare la rubrica')
    print('4 Termina programma')
    scelta = int(input('Inserire una scelta: '))
    if scelta == 1:
        key = input('Inserire il nome del contatto: ')
        value = input('Inserire il numero di telefono del contatto: ')
        rubrica[key] = value
        print('Contatto aggiunto correttamente!')
    elif scelta == 2:
        key = input('Inserire il nome del contatto da eliminare: ')
        if key in rubrica:
            del rubrica[key]
            print('Contatto eliminato correttamente!')
        else:
            print('Contatto non trovato!')
    elif scelta == 3:
        if rubrica:
            for key, value in rubrica.items():
                print(f'{key} {value}')
        else:
            print('Rubrica vuota!')
    elif scelta == 4:
        print('Programma terminato!')
        break
    else:
        print('Scelta non valida, riprova!')