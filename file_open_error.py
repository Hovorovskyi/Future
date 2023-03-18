try:
    f = open('text.txt', 'r')
    for line in f:
        if line.isdigit():
            print(line)
        elif line.isalpha():
            raise ValueError
except FileNotFoundError:
    print('File not found.')
except PermissionError:
    print('You haven`t rules to read this file.')
except ValueError:
    print('File have letter.')
except Exception as e:
    print(e, type(e))
finally:
    f.close()
