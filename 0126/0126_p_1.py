class Person:
    def __init__(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
        
p2 = Person('미상')
p2.set_name('철수')
print(p2.get_name)
# >>> <bound method Person.get_name of <__main__.Person object at 0x000001D89E007C40>>