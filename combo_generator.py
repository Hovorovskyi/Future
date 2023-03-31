from itertools import permutations


def combo_generator(combo):
    for i in permutations(combo):
        res = [int(j) for j in i]
        yield res


start = combo_generator(list(input('Enter numbers: ')))
print(next(start))
print(next(start))
print(next(start))
