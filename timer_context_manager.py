from contextlib import contextmanager
from time import time


@contextmanager
def context_man(filename, modes):
    start = time()
    try:
        file = open(filename, modes)
        yield file
        end = time() - start
        print(f"Code finish success at this time: {end}")
    except Exception as e:
        end = time() - start
        print(e, type(e))
        print(f"Code not finish, it worked at this time: {end}")
    finally:
        file.close()


with context_man('text.txt', 'r') as manager:
    print('First')

print('\n')


class TimeManager:
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode

    def __enter__(self):
        self.start = time()
        try:
            self.file = open(self.file, self.mode)
            return self.file
        except Exception as e:
            end = time() - self.start
            print(f"You have exception - {type(e)}. Work time: {end}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        end = time() - self.start
        print(f"Code finish success at this time: {end}")


with TimeManager('text.txt', 'r') as f:
    print(f.read())
