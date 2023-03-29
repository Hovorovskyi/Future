def generator(x):
    for n in range(x):
        if str(n) == str(n)[::-1]:
            yield n


for num in generator(500):
    print(num)
