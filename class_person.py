class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}. Age: {self.age}"

    def add_dog(self, dog):
        self.dog = dog

    def bark(self):
        try:
            if self.dog:
                return f"Gav"
        except Exception as e:
            print(e, type(e))
            print('Maybe you haven`t dog')


pers1 = Person('Dima', 26, 'M')
pers1.add_dog('labrador')
print(pers1.bark())
