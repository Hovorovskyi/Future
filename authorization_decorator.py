def decorator(func):
    cache = [['Dima', 111], ['Vladislav', 222]]

    def wrapper(name, password):
        nonlocal cache
        res = [name, password]
        if res in cache:
            print('Login success')
        else:
            print('Please sing in')
    return wrapper


@decorator
def autoriz(name, password):
    return f'Name: {name}, password: {password}'


try:
    name = input('Enter your name: ')
    password = int(input('Enter your password: '))
    autoriz(name, password)
except ValueError:
    print('Please, enter your password only numbers.')
except Exception as e:
    print(e, type(e))
