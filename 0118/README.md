# 데이터&제어문실습

> 20220118

## for 문

* for문의 조건과 위에서 선언한 변수를 잘 구분하자

  * ```python
    numbers = [7, 10, 22, 7, 22, 22]
    
    numbers_max = max(numbers)
    i = 0
    
    for i in numbers:
        if i == numbers_max:
            i += 1
            
    print(f'{numbers_max} {i}') 
    # 최댓값과 그 등장 횟수를 찾고 싶었지만
    # 실제로는 최댓값과 (최댓값 + 1) 이 출력됨 (선언한 변수를 for 문에 사용했기때문)
    >>>
    for num in numbers:
        if num == numbers_max:
            i += 1
    ```

* for 문으로 생성한 반복 가능한 객체를 `.join()` 을 이용해 문자열에 추가 가능

  * ```python
    word = input()
    
    word_remove_a = (alp for alp in word if alp != 'a')
    strs = "".join(word_remove_a) #반복 가능한 객체를 문자열에 더함
    print(type(word_remove_a)) #<class 'generator'> ???
    print(strs)
    ```

* 인덱스 말고 list 요소를 직접 사용하는 방법도 익숙해지자

  * ```python
    numbers = [7, 10, 22, 4, 3, 17]
    
    max_num = numbers[0]
    
    for i in range(len(numbers)-1):
        if max_num < numbers[i+1]:
            max_num = numbers[i+1]
        else:
            pass #지워도 됨
            
    print(max_num)
    # 인덱스 넘버 이용
    >>>
    for i in numbers: # 이런 경우 i 보다는 리스트 요소임을 알 수 있도록 num 등 사용
        if max_num < i:
            max_num = i
            
    print(max_num)
    # 리스트의 요소 직접 비교
    ```

* 문자열은 `+` 연산자를 이용한 편집도 가능하다

  * ```python
    word_reversed = ''
    
    for alp in word:
        word_reversed = alp + word_reversed
    # word에 저장된 단어의 순서가 뒤집힘
    ```

* 인덱스, 숫자에 유의하자(시작이 0 인지 항상 확인)

  * ```python
    number = int(input())
    total = 0
    
    for num in range(number):
        print(num)
        total += (num)
    
    print(total)
    # 총합을 구해야 하지만 range(number) 의 경우 0 ~ number - 1 까지이므로 답이 틀림
    ```

* 

