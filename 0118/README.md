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



## 데이터

* `.join()` 의 작동

  * ```python
    alps = ['a', 'b', 'c', 'd']
    strs_1 = ''.join(alps)
    
    nums = [1, 2, 3, 4]
    strs_2 = ''
    
    list_1 = []
    
    print(alps, strs_1) #['a', 'b', 'c', 'd'] abcd
    
    for num in nums:
        strs_2 = strs_2.join(num)
        print(strs_2)
        # 처음 떠올린 방법
        # 하나씩 추가하고 싶지만 정상작동 안함(반복가능한 객체도 아님)
        # join 사용법 주의
    
        list_1.append(str(num)) #타입 항상 주의
        strs_2 = ''.join(list_1)
        print(strs_2)
        # 리스트를 만들어서 추가
        
        strs_2 = strs_2 + '{0}'.format(num)
        print(strs_2)
        # 문자열 + 연산 사용
    ```

* `sorted(list)` 와 `.sort()` 의 차이?

  * ```python
    numbers = [1, 3, 2, 5, 4, 6, 7]
    tot = len(numbers)
    
    sorted_numbers = sorted(numbers)
    print(sorted_numbers) # 오름차순 정렬 작동됨
    print(numbers) # numbers 그대로
    ```

  * ```python
    numbers = [1, 3, 2, 5, 4, 6, 7]
    tot = len(numbers)
    
    sorted_numbers = numbers.sort()
    print(sorted_numbers) # None 출력
    print(numbers) # numbers가 오름차순 정렬된 리스트로 바뀜
    ```

  * 함수와 메서드의 차이?

  * `sorted()` 는 모든 이터러블을 받아들이는 반면,

  * `.sort()` 는 리스트에게만 정의되는 메서드 ([참고링크](https://docs.python.org/ko/3/howto/sorting.html))

  * 두 명령이 return 하는 값이 다른 건가?

