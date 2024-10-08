def caps_lock(funzione_parametro):
    def wrapper():
        return funzione_parametro().upper()
    return wrapper

@caps_lock
def mia_funzione():
    return 'Hello World!'

print(mia_funzione())