from class_dog import Dog


class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.dog = None

    def __str__(self):
        return f"Name: {self.name}. Age: {self.age}"

    def add_dog(self, name, breed, age):
        self.dog = Dog(name, breed, age)
        if not isinstance(self.dog, Dog):
            raise TypeError('Invalid input')


    def bark(self):
        if self.dog:
            return self.dog.bark()
        else:
            return f'{self.name} doesn`t have a dog.'


if __name__ == '__main__':
    pers1 = Person('Dima', 26, 'M')
    pers1.add_dog('Barry', 'labrador', 5)
    print(pers1)
    print(hasattr(pers1, 'dog'))
    print(pers1.bark())
