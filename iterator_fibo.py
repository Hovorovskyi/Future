class IterFibo:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        self.first = 1
        self.second = 0
        return self

    def __next__(self):
        self.first, self.second = self.second, self.first + self.second
        if self.second >= self.number:
            raise StopIteration
        return self.second


if __name__ == '__main__':
    numb = IterFibo(30)
    for num in numb:
        print(num)
