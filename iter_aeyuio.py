class MyIter:
    def __init__(self, word):
        self.word = word

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        test = 'aeyuioAEYUIO'
        if self.index == len(self.word):
            raise StopIteration
        result = self.word[self.index]
        self.index += 1
        if result in test:
            return result
        else:
            return MyIter.__next__(self)


word = "hello world"
vowels = MyIter(word)

for vowel in vowels:
    print(vowel)
