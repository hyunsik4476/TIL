class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'나는 {self.name}.'

class Mom(Person):
    gene = 'XX'
    def swim(self):
        return '엄마가 수영'

class Dad(Person):
    gene = 'XY'
    def walk(self):
        return '아빠가 걷기'

class Baby(Dad, Mom):
    # def __init__(self, name):
    #     super().__init__(name) # 이게 없어도 되는 이유?

    def swim(self): # 부모 클래스의 메소드를 덮어씌우기 가능
        return '아기가 수영'
    def crying(self):
        return '응애'

b1 = Baby('미상')
print(b1.name) # <- 왜 되는가????????????
print(b1.gene) # XY (상속받은 클래스들 중 앞의 것이 우선)
# print(b1.walk()) # 아빠
# print(b1.swim()) # 아기 (메소드가 덮어씌워졌음)
# print(b1.crying()) # 응애
    