# APS_list_2_practice

> 20220215

## 2차원 배열

* ```python
  T = int(input())
  
  for tc in range(1, T+1):
      N = int(input())
      lst = [[0]*10 for _ in range(10)]
      ans = 0
  
      for _ in range(N):
          x1, y1, x2, y2, c = map(int, input().split()) # 좌표 1, 좌표 2, 색(1 = 빨강, 2 = 파랑)
          for y in range(y1, y2+1):
              for x in range(x1, x2+1): # 인덱스 범위 조심
                  lst[y][x] += 1
                  if lst[y][x] >= 2: # 두 번 이상 체크된 곳(색이 겹친곳)
                      ans += 1 #에서 결과에 +1
  
      print(f'#{tc} {ans}')
  ```
  
* 2차원 배열 선언하고 조건에 맞는 곳에 수 더하기



## 비트 연산자를 이용한 부분집합 구하기

* 12개의 원소를 갖는 집합의 부분집합 중, 조건에 맞는 부분집합의 수 구하기

* ```python
  T = int(input())
  
  lst = [i+1 for i in range(12)]
  for tc in range(1, T+1):
      N, K = map(int, input().split()) # 부분집합 원소의 수, 원소의 합
      ans = 0
  
      for i in range(1<<12): # 경우의 수
          tot = 0
          cnt = 0
          for j in range(12):
              if i & (1<<j):
                  tot += lst[j] # 10101... 에서 1을 인덱스로 갖는 수의 합
                  cnt += 1 # 원소의 수 체크용
  
              if cnt > N or tot > K: # 조건 초과 시
                  break
  
          if tot == K and cnt == N: # 조건에 부합하면 답 + 1
              ans += 1
  
      print(f'#{tc} {ans}')
  ```

* 거의 다 맞게 풀었으나 `tot += lst[j]` 를 `tot + lst[j]` 로 오타내서 답이 안나왔음
* 비슷한 실수를 자주하는데 조심하자



## 검색

### 이진 검색(복습 필요)

* 책 페이지의 중간점을 찍는걸 반복해 target 찾기

* ```python
  def stepcnt(page, target): # 찾을 숫자 받기
      tot = 1
      l = 1
      r = page
      mid_num = int((l + r) / 2) # 중간 페이지
  
      while mid_num != target: # 찾는 숫자와 같아질때까지
          if mid_num == page-1: # pg 와 target이 같은 경우 예외처리
              tot += 1
              break
  
          tot += 1
          if mid_num > target:
              r = mid_num
  
          elif mid_num < target:
              l = mid_num
          mid_num = int((l + r) / 2)
  
      return tot
  
  T = int(input())
  
  for tc in range(1, T+1):
      pg, A, B = map(int, input().split())
      step_A = stepcnt(pg, A)
      step_B = stepcnt(pg, B)
  
      if step_A < step_B:
          print(f'#{tc} A')
      elif step_A > step_B:
          print(f'#{tc} B')
      else:
          print(f'#{tc} 0')
  ```
  
* 생각보다도 훨씬 더 헷갈림

* 처음 구현할 때, 반땅을 찍을 조건을 잘못 생각해서 한참 삽질함

* 처음 구현했던 코드:

* ```python
  def stepcnt(page, target): # 찾을 숫자 받기
      tot = 1
      l = 1
      r = page
      mid_num = int((l + r) / 2) # 중간 페이지
      tmp_num = 1 if mid_num > target else page
      prev_mid = page if mid_num < target else 1
  
      while mid_num != target: # 찾는 숫자와 같아질때까지
          # print(target, mid_num, l, r)
          tot += 1
          if mid_num > target:
              l = tmp_num
              r = mid_num
              prev_mid = mid_num
  
          elif mid_num < target:
              l = mid_num
              r = prev_mid
              tmp_num = mid_num
          mid_num = int((l + r) / 2)
  
  
      return tot
  
  
  
  T = int(input())
  
  for tc in range(1, T+1):
      pg, A, B = map(int, input().split())
      step_A = stepcnt(pg, A)
      step_B = stepcnt(pg, B)
      print(step_A, step_B)
  ```

* 



## 인덱스

### 선택 정렬(주의할 점)

* 주어진 리스트를 크기순으로 앞, 뒤 왔다갔다 하면서 출력하기

* ```python
  T = int(input())
  
  for tc in range(1, T+1):
      N = int(input())
      lst = list(map(int, input().split()))
      # 정렬하기
      for i in range(N-1):
          min_idx = i
          for j in range(i+1, N):
              if lst[j] < lst[min_idx]:
                  min_idx = j
          lst[i], lst[min_idx] = lst[min_idx], lst[i]
  
      print(f'#{tc} ', end = '')
      for k in range(5):
          a = lst[-(k+1)]
          b = lst[k]
          print(a, b, end = ' ')
      print()
  ```
  
* 선택정렬 사용해봄

* 자꾸 `if lst[j] < lst[min_idx]:` 이부분을 실수하는데 조심


