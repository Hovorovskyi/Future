try:
    f = open('test.txt', 'r')
except FileNotFoundError as e:
    print(e, type(e))
    print('Fill not found')
