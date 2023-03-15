def decorator_master(max_retries=2, exc=ValueError):

    def decorator(func):

        def wrapper(*args, **kwargs):
            try:
                for i in range(max_retries):
                    func(*args, **kwargs)
            except Exception as e:
                for i in range(max_retries):
                    print(exc)
                print(e, type(e))
        return wrapper
    return decorator


@decorator_master(3, ValueError)
def some_int():
    integer = int(input('Enter number: '))
    print(integer)


some_int()
