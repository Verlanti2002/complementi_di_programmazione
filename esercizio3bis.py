# Modificare il programma precedente in modo da usare un solo if e nessun elif

color = ['Red', 'Blue', 'Green']
val = int(input('Inserire un valore: '))
if val > 0 and val < 4:
    print(color[val-1])
else:
    print('Error')
