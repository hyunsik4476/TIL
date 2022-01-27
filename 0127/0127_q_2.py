class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')

dog = Dog('멍멍이')
bird = Bird('구구')
dog.walk()
dog.bark()
bird.walk()
bird.eat()
bird.fly()