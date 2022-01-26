# 객체지향 기초

> 20220126

## 객체?

* 객체는 특정 타입의 인스턴스(사례) 이다
  * 1, 2, 10 은 모두 int의 인스턴스
  * [1, 2, 3], [] 은 모두 list의 인스턴스



## 객체

* 객체 = 속성(Attribute) + 기능(Method)



## 1. 객체지향 프로그래밍

* 프로그래밍 패러다임의 변화 -> 무엇이 달라졌는가?
  * 데이터와 기능이 분리됨
  * 데이터를 조금 더 직접적으로 조작 가능 ex) `lst.sort()`



* 객체지향의 장점
  * 프로그램을 유연하고, 변경이 용이하게 만듬
  * 개발과 보수가 쉬워지고 직관적인 분석이 가능



## 2. 객체지향 프로그래밍 기본

* 클래스 정의 `class MyClass:`

* 인스턴스 생성 `my_instance = MyClass()`

* 메소드/ 속성 호출

  * 메소드 = 클래스 내부에 정의된 함수

  ```python
  type(my_instance)
  >>> __main__.MyClass
  ```



* 객체 비교하기

  * `==` 동등함, 변수가 참조하는 객체의 내용이 같은 경우 True

  * `is` 동일함, 변수가 같은 객체를 가리키는 경우 True (같은 주소)

    ``` python
    if a == None:
    if a is None: # 좀 더 일반적
    ```

    

## 3. 인스턴스

* 인스턴스 변수

  * 인스턴스가 가지는 속성

  * `self.<name>` 으로 정의

  * `<instance>.<name>` 으로 접근 및 할당

    

* 인스턴스 메소드

  * 호출 시, 첫 인자로 인스턴스 자기자신이 전달됨

    ```python
    ...
    	def my_method()
        	return ...
    ...
    my_instance.my_method() # 첫 인자로 self 가 전달되는 중
    >>> 마이메소드는 0개를 받을 수 있지만 1개가 전달되어 에러 발생
    ```

    ```python
    # self가 필요한 이유
    class MyClass:
    ...	
        def my_method(self)
        	return ...
    ...
    
    my_instance.my_method()
    MyClass.my_method(my_instance) # 와 동일 my_instance -> self
    ```



* 생성자 메소드

  * 객체 생성 시 자동으로 호출되는 메소드

  * `__init__` 

    ```python
    class MyClass:
        def __init__(self)
        	return ...
    ...
    my_instance = MyClass()
    ```

    ```python
    class MyClass:
        def __init__(self, name, age = 1)
        	self.name = name
            self.age = age
            print ('클래스가 생성되었습니다')
    ...
    my_instance = MyClass('name', 28) # self = my_instance
    >>> '클래스가 생성되었습니다'
    # 클래스가 선언된 순간 init 메소드가 실행되어 print 실행됨
    
    my_instance = MyClass('name')
    >>> '클래스가 생성되었습니다'
    # 함수 정의와 비슷하게 기본 값 지정 가능
    ```



* 매직 메소드
  * 특정 상황에 자동으로 실행되는 메소드
  * `__<상황>__` 
  * [참고](https://docs.python.org/ko/3.10/reference/datamodel.html#basic-customization)



## 4. 클래스

* 클래스는: 정의할 때 클래스와 해당 이름 공간이 생성



* 클래스 변수
  * 클래스 선언 내부에서 정의됨
  * 한 클래스의 모든 인스턴스가 같은 값을 가짐



* 클래스 메소드

  * 클래스를 조작하기 위한 용도

  * @classmethod 데코레이터 사용

  * 첫 번째 인자로 클래스(cls) 전달

    ```python
    class MyClass:
    ...	
        def my_method(self)
        	return self
    ...    
        @classmethod
        def class_method(cls)
        	return cls
    ...
    
    my_instance.my_method() >>> my_instance
    
    MyClass.class_method() >>> __main__.MyClass
    MyClass >>> __main__.MyClass
    ```

    

* 스태틱 메소드

  * 클래스가 사용할 메소드

  * @staticmethod 데코레이터 사용

  * 호출 시, 인자가 전달되지 않음 (= 클래스 정보에 접근 불가)

    ```python
    class MyClass:
    ...	
        def my_method(self)
        	return self
    ...    
        @staticmethod
        def static_method(static)
        	return static
    ...
    MyClass.static_mothod()
    >>> 오류 발생 # self 가 전달되지 않으므로 static 파라미터가 비어있음
    ```

    

## 5. 정리 1

* 인스턴스 메소드

  * 인스턴스 조작 용도 -> 함수 내부에 인스턴스를 던져주도록(self)

* 클래스 메소드

  * 클래스 변수 등, 클래스 조작 용도 -> 함수 내부에 클래스를 던져주도록(cls)

* 스태틱 메소드

  * 클래스/ 인스턴스 조작 용도가 아니지만 함수가 필요함

    -> 아무것도 전달되지 않음



# 객체지향 심화

## 1. 객체지향의 핵심개념

* 추상화
* 상속
* 다형성
* 캡슐화



## 2. 상속

* 두 클래스 사이의 관계(parent - child)

* 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계, 제약을 모두 상속받음
  * 종속과문강문계????
  * 이름 탐색은 인스턴스 -> 자식 클래스 -> 부모 클래스 순



* `super()` 

  * 자식 클래스에서 부모 클래스의 것을 사용하고 싶을 때

    ```python
    class Person:    
        def __init__(self, A, B):
            self.A = A
            self.B = B    
    
    class Student(Person):    
        def __init__(self, A, B, C):
            super().__init__(self, A, B) # Person 의 것 가져오기
            self.C = C
    ```



* 다중상속
  * 2개 이상의 클래스를 상속받을 수 있음
  * 메소드 이름이 겹치는 경우, 앞의 클래스의 정의가 우선됨(mro 메소드)



## 3. 다형성

* 동일한 메소드가 클래스에 따라 다르게 작동할 수 있음
  * 자식 클래스에서 메소드 오버라이딩



## 4. 캡슐화

* 외부에서의 접근을 차단하는 것?

  ```python
  class Person:
      pass
  
  p1 = Person()
  p1.name = '길동' #(x)
  >>>
  ```

  ```python
  class Person:
      def __init__(self, name):
      	self.name = name
          
      def get_name(self):
          return self.name
      
      def set_name(self):
          self.name = name
          
  p2 = Person('미상')
  p2.set_name('철수')
  print(p2.get_name) # 이렇게 쓰려면 @property 로 묶어야
  >>> <bound method Person.get_name of <__main__.Person object at 0x000001D89E007C40>>
  print(p2.get_name())
  >>> 철수
  ```

  

* protected member

  * 언더바 `_` 로 시작하는 속성

  	```python
    class Person:
      def __init__(self, name, age):
      	self.name = name
          self._age = age
          
      def get_age(self):
          return self.age
      
      def get_age(self):
          self.age = age
        
    p3 = Person('영희', 99)
    print(p3._age)
    >>> 99 # 출력은 되지만 이렇게 하지 말자는 약속

  

* private member
  * 언더바 2개 `__` 로 시작하는 속성
  
    ```python
    class Person:
      def __init__(self, name, age):
      	self.name = name
          self.__age = age
          
      def get_age(self):
          return self.age
      
      def get_age(self):
          self.age = age
        
    p3 = Person('영희', 99)
    print(p3.__age)
    >>> # 출력 안됨
    ```
  
    

# 궁금한 것

* 매직 메소드 `__gt__` 등은 둘 다 해당 클래스 안에 있을 때 호출되는가?

  * 그런 것 같음

* 다중상속 마지막에 super() 는 왜 없나?

  * 자식 클래스의 입력에 별다른 변화가 없으면 굳이 안해줘도 괜찮나?

  ```python
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
  ```

  
