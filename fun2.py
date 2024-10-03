def fun(x):
    print(x) # [1, 2]
    x.append(3)
    print(x) # [1, 2, 3]

x = [1,2]
fun(x) # la lista è passata sempre per riferimento
print(x) # [1, 2, 3]