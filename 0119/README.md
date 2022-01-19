# 함수

> 20220119

## 추상화 (Abstraction)



## 사용자 함수

```python
def function_name(parameter): # 입력
    '''
    문서화
    '''
    # code block
    # parameter 를 여기서 사용 가능
    return returning_value # 결과
```



## 함수의 반환값

* `Void funcion` 명시적인 return 값이 없는 경우 None을 반환
* `Value returning function` 함수 실행 수 return문을 통해 값 반환
* 함수를 변수에 저장할 때 무엇이 반환되는지 주의할 것

``` python
def function_name(parameter):
    # code block
    return returning_value_1 # 함수 종료
	return returning_value_2

# 함수는 하나의 값만을 반환
# returning_value_1 만 반환됨
```

```python
def function_name(parameter):
    # code block
    return returning_value_1, returning_value_2

# 하나의 튜플(returning_value_1, returning_value_2) 이 반환
```



## 함수의 입력값

* `parameter` 함수 내부에서 사용되는 이름(식별자)
* `argument` 함수 호출 시 넣어주는 값

```python
def function_name(parameter_1, parameter_2):
    # code block
    return returning_value_1

function_name('B', 'A') # 위치
function_name(parameter_2 = 'A', parameter_1 = 'B') # 키워드

# 위치 -> 키워드 가능 ex) 필수 arg.를 넣고 선택 arg.를 키워드로 지정
# 키워드 -> 위치 불가능 why?) 키워드로 지정한 순간 위치가 의미 없어짐

# 이 에러는 정의(필수/ 선택) 호출(위치/ 키워드) 모두 해당

# ============================================================== #

def function_name_2(parameter_1, *args, parameter_2):
    # code block
    return print(parameter_1, parameter_2, args)

function_name_2('B', 'C', 'D' ,'A') # 작동 안함
function_name_2('B', 'C', 'D' , parameter_2 = 'A')
# 작동 함 >>> B A ('C, 'D')
function_name_2(parameter_2 = 'A', parameter_1 = 'B')
# 작동 함 (왜???) >>> B A ()

# ============================================================== #

def function_name_3(parameter_1, parameter_3 = 'C', parameter_2): #SyntaxError: non-default argument follows default argument
    # code block
    return print(parameter_1, parameter_2, parameter_3)

function_name_3('B', 'A') # 작동 안함
function_name_3(parameter_2 = 'A', parameter_1 = 'B') # 작동 안함
```

* 기본값을 지정하면 함수 호출 시 argument 값을 설정하지 않아도 됨

``` python
def function_name(parameter_1, parameter_2 = 0):
    # code block
    return parameter_1 + parameter_2

function_name(1) # return 1 (parameter_2 = 0 기본값 적용)
function_name(1, 2) # return 3
```

* 패킹/ 언패킹 연산자(`*`)를 이용해 다수의 argument 를 받을 수 있음

``` python
def function_name(*args): # 권장되는 기입 형태
    # code block
    return returning_value

# args 는 튜플 (입력이 1개여도 (A, )형태의 튜플임)
```

```python
def function_name(**kwargs): # 권장되는 기입 형태
    # code block
    return print(kwargs) # **kwargs가 아님

function_name('name': '홍길동', 'age': 999) 
# 잘못된 용례(Invalid syntax)

# function_name('name' = '홍길동', 'age' = 999) 
# 잘못된 용례 2

function_name(name = '홍길동', age = 999)
# 바른 용례 (이 때 name 과 age는 식별자)

function_name()
# 도 가능 (빈 딕셔너리 {} 가 리턴)

# kwargs 는 딕셔너리
# 호출 과정에서 dictionary를 정의하는 것이 아니라 식별자를 넣어주는 것
```



## 함수의 범위

* 코드 내부에 `local scope` 생성
* 변수 역시 `local` 과 `global` 이 구분됨

```python
def ham():
    a = 'spam' # 로컬 변수
    # 3.
    return a # 여전히*2 오류
    
# 1.    
print(a) # NameError
# 2.
ham()
print(a) # 여전히 NameError

# 블랙박스의 결과를 받아보고 싶으면 반환 값을 변수에 저장
# 결과를 주고 싶으면 return 할것
```

* `Local`, `Enclosed`, `Global`, `Built-in` LEGB Rule

```python
a = 'global a'
b = 'global b'
c = 'global c'

def en_fn():
    a = 'enclosed a'
    b = 'enclosed b'

    def lo_fn():
        a = 'local a'
        print(a, b, c)

    lo_fn()

    print(a, b, c)
    

en_fn()

print(a, b, c)

# 출력: 변수의 탐색 순서에 주의
# local a enclosed b global c
# enclosed a enclosed b global c
# global a global b global c
```

* `global` 문

```python
a = 'richam'

def ham():
    global a
    a = 'spam'
        
print(a) # 'richam'
ham()
print(a) # 'spam'

# 알고리즘 등 문제풀이가 편해지는 경우엔 사용
# 다만, 그 외에는 가급적 사용하지 않는 것을 권장 (블랙박스의 rule을 깨는 것)
# return 해서 받아서 쓰는게..?
```



## 함수의 문서화

* Documentation String
* 주피터 노트북에서 `Shift` + `Tab` 으로 확인 가능

### 이름짓기

* 상수 이름은 전체 대문자
* 클래스, 예외의 이름은 첫 글자 대문자
* 이외 나머지 소문자 + `_`



## 함수 응용

* `map(function, iterable)`

  * 순회 가능한 데이터구조의 모든 요소에 함수 적용하고 map object를 반환

  * ```python
    input_value = map(int, input().split())
    print(list(input_value))
    <<< 20 20
    >>> [20, 20] # 정수형
    ```

* `filter(function, iterable)`

  * 순회 가능한 모든 요소에 함수 적용, 결과가 True인 것들을 filter object로 반환

* `zip(*iterables)`

  * 복수의 iterable 을 모아 튜플을 원소로 하는 zip object 반환

* `lambda [parameter] : <표현식>`

  * 일시적으로 사용할 함수를 정의 가능

  * ```python
    # 람다함수 w/ 필터
    def odd(n):
        return n % 2 # ???
    
    print(list(filter(odd, range(5))))
    # 이게 왜 작동하나?
    # 첫 추측: return 1 = n, return 0 =None ???
    # print(odd(n)) 으로 확인해봄 -> 아님
    # 해결: filter 함수에서 function 은 T/ F 판단
    
    print(list(filter(lambda n: n % 2, range(5))))
    
    print(list(filter(lambda n: n  if n % 2 == 1 else None, range(5))))
    # 실상 이럴 필요가 없었음: n % 2 == 1 자체가 T/ F 를 반환하므로
    # n 을 리턴하는 것에 대해: filter 함수의 동작에 대한 이해 부족
    ```

* 재귀 함수

  * 자기 자신을 호출하는 함수

  * 한 개 이상의 종료되는 상황(base case)가 존재하고, 수렴하도록 작성

  * ```python
    # 재귀함수
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1) 
            
    # 팩토리얼 함수 안에서 팩토리얼 함수 호출
    # 함수는 return 값이 정해져야 종료될 수 있으므로
    # n, n - 1, ... , 1 로 수렴해 base case에 도달 (factorial(1))
    ```

  * `stack overflow` 메모리 스택이 넘치게 되면 프로그램이 멈춤

  * 파이썬의 최대 재귀 깊이는 1,000번, 이를 넘어가면 recursion error 발생

  * 왜 쓰는가? >>> 알고리즘 상 자연스러운 경우/ 변수 숫자 감소



# 모듈

## 모듈과 패키지

* `모듈` 특정 기능을 하는 코드를 파이썬 파일 단위로 작성한 것
* `패키지` 여러 모듈의 집합



## 모듈 불러오기

* ```python
  import pprint
  pprint.pprint('a')
  ```

* ```python
  from pprint import pprint # from 모듈명 import 함수명
  pprint('a')
  ```

* ```python
  from pprint import * # 모듈명 내의 모든 함수
  pprint('a')
  ```



## 파이썬 패키지 관리자 (pip)

* ```bash
  $ pip freeze > requirements.txt
  $ pip install -r requirements.txt
  ```



## 가상환경

* `venv` 가상환경 모듈

  * ``` bash
    $ python -m venv venv # venv라는 이름의 가상환경 폴더 생성
    $ pip list # 아직 내 컴퓨터
    
    $ source venv/Scripts/activate # 가상환경 활성
    $ pip list # venv 환경에 깔린 pip 리스트 보여줌
    ```

