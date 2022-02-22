# APS_stack_practice

> 20220222

## 2차원 배열에서 특정 방향으로 ~만큼 

* ```python
  for y in range(N):
        for x in range(M):
            tot = arr[y][x]
            for k in range(1, arr[y][x]+1):
                for dy, dx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nx = x+dx*k
                    ny = y+dy*k
                    if M>nx>=0 and N>ny>=0:
                        tot += arr[ny][nx]

* 어떤 전형적인 형태
* 오류를 피하기 위해 arr에 접근하기 전 유효성 검사부터 할 것



## 스택 연습 1

* ```python
      stack = [0]*N       # 저장용 스택
      top = -1            # 현재 위치
      ans = 1             # 답 판별용 변수
  
      for i in range(N):  # 문자열 내의 모든 문자에 대해서
          if strs[i] == '(' or strs[i] == '{':    # 문자가 여는괄호면
              top += 1                            # 스택 포인터 이동 후
              stack[top] = strs[i]                # 해당 여는괄호 저장
  
          elif strs[i] ==')':                     # 닫는소괄호인 경우
              if stack[top] == '(':               # 마지막에 저장된 괄호가 여는소괄호면
                  stack[top] = 0                  # 지우고
                  top -= 1                        # 스택포인터 이동
              else:
                  ans = 0                         # 마지막 저장된게 닫는소괄호가 아니면
                  break                           # 답=0, 판별 종료
  
          elif strs[i] == '}':                    # 중괄호에 대해 같은 일 수행
              if stack[top] == '{':
                  stack[top] = 0
                  top -= 1
              else:
                  ans = 0
                  break
  ```

* 특정 문자에 대한 검사

* 0 으로 초기화된 stack 과  top 사용하는 연습



## 스택 연습 2

* ```python
  lst = list(input())
  N = len(lst)
  check = [0]*N   # 스택용 빈 통 만들기
  top = -1        # 스택의 현재 위치
  ans = 0         # 남은 글자의 수
  for i in range(N):
      if lst[i] != check[top]:    # 스택의 최상단 글자가 문자열과 다르면
          top += 1                # 다음 위치로
          ans += 1
          check[top] = lst[i]     # 스택에 추가
      else:                       # 스택의 최상단 글자가 문자열과 같으면
          check[top] = 0          # 최상단 문자 0으로 초기화
          top -= 1                # 현재 위치 -1
          ans -= 1
  # print(f'{ans}')
  print(f'{top+1})
  ```

* top 으로 스택을 사용하게 되면 굳이 len이나 ans 에 단계를 누적하지 않아도 된다



## 메모이제이션

* ```python
  def facto(n):       # 팩토리얼 함수
      if n == 1:
          return 1
      if memo[n] == 0:
          memo[n] = n*facto(n-1)  # 연습
      return memo[n]
  
  
  T = int(input())
  N_max = 30
  memo = [0]*(N_max+1)            # 메모 저장
  memo[0] = 1
  ```

* 팩토리얼 함수를 만드는 과정에서 memoization 연습
