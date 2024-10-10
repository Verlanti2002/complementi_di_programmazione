# Implementare un decoratore chiamato @log_execution che: 
    # 1. ogni volta che la funzione decorata viene eseguita, scrive su un file di log
    #    (es. "execution_log.txt") la data e l'ora di esecuzione, insieme al nome della funzione eseguita e agli argomenti passati
    # 2. Applicare questo decoratore a una funzione che accetta un qualsiasi numero di argomenti e li somma

def log_execution():
    def wrapper(*args, **kwargs):
        file = open('execution_log.txt', 'w')
        file.write()        



@log_execution
def function():