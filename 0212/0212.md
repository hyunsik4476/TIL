# APS

## 그리디

* 현재 가장 좋아보이는 것을 고르고, 나중에 미칠 영향에 대해선 고려X
* 정렬, 최단 경로 찾기 등과 다르게 특정 알고리즘을 암기한다고 풀 수 있다고 장담할 수 없음



### 예제 1. 거스름돈

> 500원, 100원, 50원, 10원짜리로 가장 적은 수의 동전으로 거슬러주기

* 가장 큰 화폐 단위부터 돈을 거슬러주면 자연스럽게 가장 적은 수의 동전으로 거슬러줄 수 있다

* ```python
  money = ???
  cnt = 0
  coin_list = [500, 100, 50, 10]
  
  for coin in coin_list:
      cnt += money//coin
      # money -= coin*cnt
      # 아래와 같이 나머지를 사용하면 됨
      money %= coin
  ```

* 하지만, 화폐 단위가 배수가 아니라면? 탐욕 알고리즘으로 찾은 답이 최적이 아닐 수도 있다

* 항상 자신이 찾은 해의 정당성을 다시 한 번 확인해볼것



### 예제 2. 숫자 더하기

> 주어진 N개의 숫자를 M번 더해 가장 크게 만들 수 있는 해 구하기
>
> 단, 하나의 인덱스에 있는 숫자가 K번 초과해서 연속으로 사용될 수 없다

* 위와 비슷하게 큰 수부터 더하는 형태로 풀기로 함

* ```python
  N, M ,K = map(int, input().split())
  data = list(map(int, input().split()))
  ans = 0
  
  data.sort()
  max_1 = data[-1] # 가장 큰 수
  max_2 = data[-2] # 두번째로 큰 수
  
  # m1+m1+m1+m2+m1+m1 처럼 될 수 있다
  
  i = 0
  while 1:
      for _ in range(K):
          if i == M:
              break
          ans += max_1
          i += 1
  
      if i == M:
          break
      ans += max_2
      i += 1
  
  print(ans)
  ```

* i를 새로 선언하는 것보다 m에서 1씩 빼는게 더 좋았을 것

* 이런 방식의 문제점은 M이 커지면 시간이 오래 걸린다는것



* 방법 2

* ```python
  N, M ,K = map(int, input().split())
  data = list(map(int, input().split()))
  ans = 0
  
  data.sort()
  max_1 = data[-1] # 가장 큰 수
  max_2 = data[-2] # 두번째로 큰 수
  
  # m1+m1+m1+m2+m1+m1 처럼 될 수 있다
  # m1이 몇 번 더해지는지 알 수 있을까?
  # M 을 K로 나눈다?
  ans = max_1*(K*M//(K+1) + M%(K+1)) + max_2*(M//(K+1))
  print(ans)
  ```

* 문제를 풀 때 한 번 더 생각해보자



### 카드 뽑기

> N개의 행, M개의 열을 가진 카드 더미가 주어짐 (M*N)
>
> 먼저 행을 선택하고 행에 포함된 카드 중 가장 숫자가 낮은 카드를 뽑는다

* 주어진 지문이 길지만 해결하기 위한 조건이 간단한 편

* ```python
  N, M = map(int, input().split())
  lsts = [0]*N
  for i in range(N):
      lsts[i] = list(map(int, input().split()))
  
  ans = min(lsts[0])
  for j in range(N):
      tmp = min(lsts[j])
      if tmp > ans:
          ans = tmp
  print(ans)
  ```

* for 문 안에서 매번 한 줄씩 입력을 받아와 최소값을 저장해도 된다



### 1이 될 때까지

> 어떤 수 N이 1이 될 때까지 N-1 혹은 N/K 중 하나의 연산을 한다
>
> 단, N/K는 N이 K로 나누어 떨어질 때만 실행할 수 있다
>
> 이 때 최소한의 연산 횟수를 구하자

* ```python
  N, K = map(int, input().split())
  ans = 0
  
  while N != 1:
      if N % K == 0:
          N //= K
          ans += 1
      else:
          N -= 1
          ans += 1
  print(ans)
  ```



* 만약 N이 엄청 크다면?

* K의 배수가 되기까지의 연산 과정을 줄여보자

* ```python
  N, K = map(int, input().split())
  ans = 0
  
  while N != 1:
      remain = N % K
      if remain == 0:
          N //= K
          ans += 1
      else:
          N -= remain
          ans += remain
  
  print(ans)
  ```

