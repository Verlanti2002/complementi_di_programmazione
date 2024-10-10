# Scrivere una funzione chiamata create_multiplier che: 
    # 1. accetta un numero come argomento
    # 2. restituisce una closure 
# Questa closure deve accettare un altro numero e restituire il prodotto dei due numeri
# Esempio:
# $- multiply_by_3 = create_multiplier(3)
# $- print(multiply_by_3(10)) # Output: 30

def create_multiplier(a):
    def product(b):
        return a * b
    return product

multiply_by_3 = create_multiplier(3)
print(multiply_by_3(10))