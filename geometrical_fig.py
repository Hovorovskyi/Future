from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def __str__(self):
        return f'Obj: {Shape.__class__.__name__}'


class Rectangle(Shape):
    def __init__(self, name, color, width, height):
        super().__init__(name, color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimetr(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Obj: {self.name}. Color: {self.color}. Area: {self.area()}. Perimetr: {self.perimetr()}'


class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimetr(self):
        return 3.14 * 2 * self.radius

    def __str__(self):
        return f'Obj: {self.name}. Color: {self.color}. Area: {self.area()}. Perimetr: {self.perimetr()}'


class Square(Shape):
    def __init__(self, name, color, side):
        super().__init__(name, color)
        self.side = side

    def area(self):
        return 0.5 * self.side*2

    def perimetr(self):
        return 4 * self.side

    def __str__(self):
        return f'Obj: {self.name}. Color: {self.color}. Area: {self.area()}. Perimetr: {self.perimetr()}'


if __name__ == '__main__':
    circle1 = Circle('circle', 'red', 5)
    rectangle1 = Rectangle('rectengle', 'green', 2, 4)
    square1 = Square('square', 'yellow', 5)
    test = [circle1, rectangle1, square1]
    for fig in test:
        print(fig)
