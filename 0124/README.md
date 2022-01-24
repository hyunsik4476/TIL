# 데이터 구조

> 20220124

## 문자열

* 기본적으로  immutable 이므로 새로운 문자열을 반환

* ```python
  a = ' apple banana juice '
  print(a.find('b'))
  print(a.find('A'))
  
  lst_1 = a.split()
  lst_2 = a.split('j')
  print(lst_1) # ['apple', 'banana', 'juice']
  print(lst_2) # [' apple banana ', 'uice ']
  
  a_1 = a.replace('a', 'z', 3)
  print(a)
  print(a_1) # 맨 끝 count 수 만큼 a 가 z로 변경(미입력이 모든 a가 변경)
  
  a_2 = a.strip() # 공백문자 제거
  a_3 = a.strip('a')
  a_4 = a.strip(' a')
  print(a_2) # 'apple banana juice'
  print(a_3) # ' apple banana juice '
  print(a_4) # 'pple banana juice '
  
  b = ''.join('HELLo')
  b_1 = '!'.join('HELLo')
  b_2 = '!'.join(['h', 'e', 'l', 'l', 'o'])
  print(b)
  print(b_1)
  print(b_2)
  ```

* 

## 리스트

* `.append(요소)`
* `.extend(iterable)` # 문자열을 넣으면 하나하나 분리돼서 들어감
* `.insert(idx, x)` # idx가 리스트 길이보다 크면 맨 뒤에 추가
* `.remove(x)` # x 가 없는 경우 ValueError 발생
* `.pop(idx)` # idx 미 기입시 마지막 항목 반환, 삭제
* `.clear()` # 모든 값 삭제



* `.index(x)` # x 값을 찾아 해당 값의 인덱스를 반환
* `.count(x)` # x 값의 개수를 반환함
* `.sort()` # 원본 리스트를 정렬, None 반환 (함수 sotred()와 구분할 것)
* `.reverse()` # 원본 리스트를 두집음



## 튜플

* 변경할 수 없으므로 값에 영향을 미치지 않는 메소드만 지원
* 즉, `.extend()` 같은건 지원 안함

 ## 셋

* 순서가 없음 !!!!!!!!!!!!!!!!
* `.add(x)` # x가 셋에 없다면 추가
* `.pop()` # 임의의 항목을 반환하고, 제거 (순서가 없음!!!!!!!!!!!!!!!)
* `.add(item)` # 값 1개를 추가
* `.update(*others)` # 값 여러개를 추가
* `.remove(elem)` # 셋에서 삭제하고 , 없으면 키 에러
* `.discard(elem)` # 셋에서 삭제하고, 없어도 에러 X
* `.pop()` 임의의 원소를 제거해 반환



## 복사

* 리스트2 = 리스트1 와 같이 =을 통해 복사한 경우
  * 리스트2의 요소를 바꾸면 리스트 1도 바뀜
  * -> 해당 객체에 대한 객체 참조를 복사 (얕은 복사)
* 리스트1 = []
* 리스트2 = copy.deepcopy(리스트1) # import copy 필요
  * 리스트2의 요소를 바꿔도 리스트1은 바뀌진 않음
* 어떤 주소의 object를 참조하고 있는지 명확히 알 필요가 있음



 # 에러, 예외처리

* 에러: SyntaxError가 발생하면, 실행이 되지 않음
* 예외: 실행 중에 감지되는 에러들을 예외 라고 부름
  * ex) 제로디비전
* `try`, `except`, `finally`
  * 한 개의 `try` 문엔 반드시 하나 이상의 `except` 필요
* `raise` 강제로 예외 이름을 넣고 발생 (실제 프로덕션 코드에서 활용)
* `assert` 어떤 조건이 거짓이면 발생 (내부, 테스트용)



# 그 외

* 오늘도 멋지게 딕셔너리 쓰기 실패
