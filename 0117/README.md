# 데이터 & 제어문

> 20220117

## 1. 자료형

### 불린형(Boolean)

* `True` 와 `False` 값을 가짐

* `0`, `0.0`, `()`, `[]`, `{}`, `''`, `None` 은 `False`로 변환



### 수치형(Numeric)

#### 정수(interger)

* `int` 타입

* 오버플로우가 발생하지 않음

* 진수 표현
  * 2진수: 0b
  * 8진수: 0o
  * 16진수: 0x
  
  

#### 부동소수점, 실수(float)

* `float` 타입

* 부동소수점 연산 과정에서 floating point rounding error 발생 가능

  * `abs(a-b) <= sys.float_info.epsilon` 과 같이 매우 작은 수와 비교

  * 혹은 math 모듈을 활용하자

  * ```python
    import math
    math.isclose(a, b)
    ```



#### 복소수(complex)

* 파이썬에서 허수부는 `j`로 표현



### 문자열(String)

* 모든 문자는 `string` 타입

* Immutable(불변), Iterbale(반복 가능) 한 속성을 갖는다.

* ```python
  print('''
  과 같이 3개의 '작은따옴표' 혹은 "큰 따옴표" 묶어
  줄바꿈 등에 편리하게 사용 가능하다.
  ''')
  ```

* Escape sequence

  * 문자열 내에서 특정 문자, 조작을 위함
  * `\n` 줄 바꿈
  * `\t` 탭
  * `\\` `\`
  * `\'` `'`
  * `\"` `"`

* 문자열 포맷

  * ```python
    # %-formating
    print('%s') % name
    ```

  * ```python
    # .format()
    print('{0} afasfew {1}'.format(1, 2))
    ```

  * ```python
    # f-string
    print(f'My name is {name}.')
    ```





### None

* 자료형 중 하나, 반환 값이 없는 함수에서도 사용



## 2. 제어문

### 조건문(if)

* 참/ 거짓을 판단할 수 있는 조건식과 함께 활용한다.

* 들여쓰기로 코드블럭 구분에 유의

* `if` 문 조건의 boolean 판단 (`1. 자료형`의 `Boolean` 참조)

  * ```python
    my_list = []
    if my_list:
        print('비어있지 않은 리스트 입니다.'')
    else:
        print('빈 리스트 입니다.')
    ```


#### 조건 표현식

* <true인 경우 값> if <expression> else <false인 경우 값>

  * ```python
    my_list = []
    ans = '비어있지 않은 리스트 입니다.' if my_list else '빈 리스트 입니다.'
    print(ans)
    ```

* 가독성 개선을 위함, 억지로 쓸 필욘 없음



### 반복문(while, for)

#### While

* 종료 조건이 필요



#### For

* 시퀀스(string, tuple, list, range)를 포함한 순회가능한(iterable) 객체 요소를 모두 순회함
  * 딕셔너리의 경우 기본적으로 key를 순회함
* `enumerate(list_name)`를 통해 `(index, 요소)` 형태의 튜플을 받아 순회 가능



#### List/ Dictionary comprehension

* ```python
  list = [number for number in range(n)] #list
  ```

* ```python
  dictionary = [number: number * 2 for number in range(n)] #dictionary
  ```



#### 반복문 제어

* `break` 반복문 종료
* `continue` 컨티뉴 이후의 코드블록을 수행하지 않고 다음 반복을 수행
* `pass` 아무것도 하지 않음 (자리 채우기 용도로 사용 가능)
* `for` - `else` 에서 `else`문은 루프가 `break` 로 중단되면 실행되지 않음





# 3. 주피터 노트북

## 실행하기

* 원하는 폴더에서 CLI에 `jupyter notebook` 입력



## 단축키

* `H`(help): 단축키 도움말

* `B`(below): 아래 셀 추가

* `A`(above): 위에 셀 추가

* `DD`(delete): 셀 추가

* `ctrl` + `Enter`: 실행

* `M`: python -> markdown 셀 변환

* `Y`: markdown -> python 셀 변환



## 사용하기

* `In []`안의 숫자: 실행 넘버

* `Out[]`은 실제 출력이 아닌  마지막 줄의 내용을 보여줄 때 표시

  * ```python
    a = 2 + 3
    a
    >>> Out[1] 5
    ```
