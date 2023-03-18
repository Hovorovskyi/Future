def debug_master(initial):

    def debug(func):

        def wrapper(x, y):
            if initial is True:
                print(f"Input: ({x}, {y})")
            elif initial is False:
                print(func(x, y))
        return wrapper
    return debug


@debug_master(False)
def add(x, y):
    return x + y

add(3, 2)
