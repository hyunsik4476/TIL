# APS_stack

> 20220221

## 스택의 특성

* 자료를 삽입하거나 꺼낼 수 있다
* 마지막에 삽입한 자료를 가장 먼저 꺼낸다
* 

## 스택의 구현

* 자료구조: 자료를 선형으로 저장할 저장소

  * 배열을 사용할 수 있다

  * 스택에서 마지막 삽입된 원소의 위치를 stack pointer(top)이라 부른다




* ```python
    stack = []
    stack.append(10)
    #...
    stack.pop()
    ```

* ```python
    top = -1
    stack = [0] * 10
    
    top += 1
    stack[top] = 10
    
    top += 1
    stack[top] = 20
    #...
    print(stack[top])
    top -= 1
    ```

  

## 스택의 응용

### 괄호검사

* 여는 괄호를 만나면 스택에 삽입, 닫는 괄호를 만나면 스택에서 제거
* 닫는 괄호를 만났을 때 스택이 비어있거나, 끝까지 가서 스택에 괄호가 남아있으면 false



### 함수의 호출과 복귀

* 



## 재귀호출

* 마지막에 구한 하위 값을 이용하여 상위 값을 구하게 됨
* 피보나치/ 팩토리얼을 구하는 재귀함수도 이에 속함
* 단, `function(현재idx, 목표 idx)` 형태가 조금 더 일반적이다
  * 피보나치/ 팩토리얼의 경우 목표가 0/ 1로 이미 정해져 있기 때문에 그런 형태가 된 것

* ```python
  def fn(i, N):
      if i == N:
          print(B)
      else:
          B[i] = A[i]
          fn(i+1, N)
          
  A = [1, 2, 3]
  B = [0]*3
  fn(0, 3)
  # >>> [1, 2, 3]
  ```



## Memoization

* 재귀 호출에서 중복된 호출을 줄이기 위한 방법

* 이미 계산한 값을 저장하겠다

* ```python
  def fibo1(n):
      global memo
      if n >= 2 and len(memo) <= n:	# append로 접근하고 있으므로 아직 저장 안된 단계에 대해
          memo.append(fibo1(n-1) + fibo1(n-2))
      return memo[n]					# 이미 저장된 단계의 경우 바로 여기로 넘어옴
  
  memo = [0, 1]	# fibo1(0) = 0, fibo1(1) = 1
  ```

* ```python
  def fibo1(n):
      global memo
      if n >= 2 and memo[n] == 0:
          memo[n] = (fibo1(n-1) + fibo1(n-2))
      return memo[n]
  
  memo = [0] * (N+1)
  memo[0] = 0
  memo[1] = 1
  ```



## DP(Dynamic Programming)

* 동적 계획(DP) 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘이다

* 작은 부분 문제들을 해결하여 최종적으로 원래의 문제를 해결



### 예시) 피보나치 수 DP 적용해보기

1. 문제를 부분 문제로 분할
2. 가장 작은 부분 문제부터 해를 구한다
3. 결과를 테이블(리스트)에 저장하고 저장된 부분 문제의 해로 상위 문제의 해를 구한다

* ```python
  N = 10
  fibo = [0]*(N+1)
  fibo[0] = 0
  fibo[1] = 1
  for i in range(2, N+1):
      fibo[i] = fibo[i-1] + fibo[i-2]
  ```

* 반복문을 사용해 해결이 가능하므로, 함수의 호출/ 복귀 시간이 필요 없다
