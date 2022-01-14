# 파이썬 기초

> 202201014

## hello.py

* 변수에 저장하기
* `print()` 로 출력하기
* n번 반복해보기
  * `while`과 `for`은 종료조건 필요여부로 나뉨
  * Python의 `for`와 `range`에 익숙해지자

## lunch.py

* 리스트 만들어보기

* 리스트 요소의 타입에 주의하자

  * `type()`으로 확인해보는 습관을 갖자

* 함수 사용을 위해 모듈 호출해보기

  * `import random`으로 `choice`와 `sample`함수 써보기

    ```python
    import random
    
    lunch_box = ['햄버거', '피자', '치킨']
    
    today_menu = random.choice(lunch_box)
    
    print(today_menu)
    ```

    

## phone.py

* 딕셔너리 만들어보기

  ```python
  dictionary = {'key1': 'value1', 'key2': 'value2', ...}
  dictionary[key1] # == value1
  ```

* 요소의 타입에 주의하자

* key는 중복이 불가능

* value로 key 알아내기

  ```python
  print([key for key, value in dictionary.items() if value == ('value1')])
  ```



## dust.py

* `if`, `elif`, `else` 써보기
* `def funcion()`로 함수 만들어보기



## lotto.py

* `random.sample(list, number)`로 list 에서 number만큼 무작위 뽑기
* `list(range(x, y))`사용해보기