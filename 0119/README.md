# 함수

> 20220119

## Abstraction (추상화)



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

function_name(B, A) # 위치
function_name(parameter_2 = A, parameter_1 = B) # 키워드

# 위치 - > 키워드 가능 ex) 필수 arg.를 넣고 선택 arg.를 키워드로 지정
# 키워드 -> 위치 불가능 why?) 키워드로 지정한 순간 위치가 의미 없어짐

# 이 에러는 정의(필수/ 선택) 호출(위치/ 키워드) 모두 해당
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

