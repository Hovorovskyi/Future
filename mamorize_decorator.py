def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(cache[args])
        else:
            result = func(*args)
            cache[args] = result
            print(result)

    return wrapper


@memoize
def add(x, y):
    return x + y


add(3, 2)
add(3, 2)
add(3, 2)
