class Dog:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"Name is: {self.name}. Breed is: {self.breed}"


dog1 = Dog('Honye', 'labrador', 5)

print(dog1.bark())
