# Modificare il programma precedente in modo da non usare if

diz = {1: 'Red', 2: 'Blue', 3: 'Green'}
val = int(input('Inserire un valore: '))
print(diz.get(val, 'Errore, valore non valido!'))
