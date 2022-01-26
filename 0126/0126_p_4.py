class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        if self.age > other.age:
            return f'{self.name}가 더 늙었습니다.'

p1 = Person('철수', 99)
p2 = Person('영희', 999)
print(p2 > p1)