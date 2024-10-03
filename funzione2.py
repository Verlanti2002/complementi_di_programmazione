# Scrivere un decoratore che arricchisca una funzione come segue:
#   1) Oltre a ritornare il risultato della funzione stessa, lo stampa anche a video
#   2) Prima di eseguire chiede all'utente se vuole modificare il parametro in ingresso (opzione non possibile se vi sono più parametri)

def decoratore(func):
    def wrapper(*args, **kwargs):
        # Verifica se la funzione ha un solo parametro
        if len(args) == 1 and len(kwargs) == 0:
            modifica = input(f"Vuoi modificare il parametro '{args[0]}'? (si/no): ").lower()
            if modifica == 'si':
                nuovo_parametro = input("Inserisci il nuovo valore: ")
                try:
                    # Prova a convertire il nuovo parametro nel tipo del vecchio parametro
                    args = (type(args[0])(nuovo_parametro),)
                except ValueError:
                    print("Errore: impossibile convertire il parametro nel tipo corretto.")
                    return
        
        # Esegue la funzione originale
        risultato = func(*args, **kwargs)
        
        # Stampa il risultato a video
        print(f"Risultato: {risultato}")
        
        # Ritorna il risultato della funzione
        return risultato
    
    return wrapper

@decoratore
def square(n):
    return n**2

square(4)