num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

try:
    res = num1 / num2
    print(res)
except ZeroDivisionError as e:
    print(e, type(e))
    print('Can`t use Zero')
except Exception as e:
    print(e, type(e))
