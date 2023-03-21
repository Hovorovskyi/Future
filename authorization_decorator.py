def decorator(func):
    cache = [['Dima', 111], ['Vladislav', 222]]

    def wrapper(*args):
        name = input('Enter your name: ')
        password = int(input('Enter your password: '))
        nonlocal cache
        res = [name, password]
        if res in cache:
            print('Login success')
        else:
            print('Please sing in')
    return wrapper


@decorator
def autoriz():
    print('Hello')


autoriz()
