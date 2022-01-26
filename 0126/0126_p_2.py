from tkinter import N


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    @property # 메소드지만 속성처럼 쓸 수 있게 해줌????
    def name(self):
        return self._name

    @property # 메소드지만 속성처럼 쓸 수 있게 해줌????
    def age(self):
        return self._age

    @age.setter # 이 함수가 위에 정의되어 있어야 사용 가능
    def age(self, n_age):
        self._age = n_age
        
p2 = Person('미상',10)
print(p2.name) # 프로퍼티
print(p2._name) # 직접 접근
print(p2.age) # 프로퍼티
p2.age = 99 # 세터
print(p2.age)