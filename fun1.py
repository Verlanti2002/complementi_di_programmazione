def fun(x): 
    print(x) # 5
    x = 'ciao' # viene modificata la x locale (passaggio per valore)
    print(x) # 'ciao'

x = 5
fun(x)
print(x) # 5