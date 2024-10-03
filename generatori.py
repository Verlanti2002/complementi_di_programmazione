def range(stop):
    i = 0
    while i < stop:
        yield i
        i = i + 1

for num in range(5):
    print(num)
