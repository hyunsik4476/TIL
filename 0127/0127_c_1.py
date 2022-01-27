class Doggy:
    nums_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, jong):
        self.name = name
        self.jong = jong
        self._age = 1
        Doggy.nums_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def bark(self):
        print('왈왈!')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, n_age):
        self._age = n_age

    @classmethod
    def __del__(cls):
        cls.nums_of_dogs -= 1

    @classmethod
    def get_status(cls):
        return f'Brith: {cls.birth_of_dogs}, Current: {cls.nums_of_dogs}'

d1 = Doggy('초코', '푸들')
d2 = Doggy('꽁이', '말티즈')
d3 = Doggy('별이', '시츄')

print(Doggy.get_status())
print(d1.get_status())
del d3
print(Doggy.get_status())
print(d1.get_status())
d1.bark()
d1.age = 99
print(d1.age)