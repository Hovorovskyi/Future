def decorator(func):
    counter = 0

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        nonlocal counter
        counter += 1
        print(counter)
    return wrapper


@decorator
def say_hi():
    print('Hello, my friend')


say_hi()
say_hi()
say_hi()
say_hi()
say_hi()
