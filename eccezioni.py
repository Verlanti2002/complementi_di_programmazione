try:
    print("Esecuzione del blocco try")
    # Nessuna eccezione sollevata
except ValueError:
    print("Gestione dell'eccezione ValueError")
except TypeError:
    print("Gestione dell'eccezione TypeError")
else:
    print("Il blocco try è andato a buon fine, eseguo l'else")
finally:
    print("Il blocco finally viene eseguito in ogni caso")