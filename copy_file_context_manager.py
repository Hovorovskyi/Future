class CopyContextManager:
    def __init__(self, file1, mode1, file2, mode2):
        self.file1 = file1
        self.file2 = file2
        self.mode1 = mode1
        self.mode2 = mode2

    def __enter__(self):
        self.bunker = ''
        self.file_1 = open(self.file1, self.mode1)
        self.file_2 = open(self.file2, self.mode2)
        for line in self.file_1:
            self.bunker += line
        return self.file_1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_2.write(self.bunker)
        self.file_1.close()
        self.file_2.close()


with CopyContextManager('text.txt', 'r', 'bunker.txt', 'a') as f:
    print(f.read())
