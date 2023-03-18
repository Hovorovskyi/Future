num = input('Enter number: ')

try:
    print(int(num))
except ValueError as e:
    print('Enter number, not letter')
except Exception as e:
    print(e, type(e))
