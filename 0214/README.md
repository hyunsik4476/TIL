# APS_list_2

> 20220214

## 2차원 배열

* ```python
  lst_2 = [[0]*n]*n # X
  lst_2 = [[0]*n for _ in range(n)] # O
  ```

* 이런 식으로 선언해야함



## 2차원 배열의 접근

* 행 우선 순회
* 열 우선 순회

### 지그재그 순회(???)

* ```python
  for i in range(y):
      for j in range(x):
          lst[i][j + (x-1- 2*j) * (i%2)] # 지그재그 순회
          # 						i값(y축 번호) 에 따라 j가 될지 x-1 - j 가 될지 결정
  ```



### 델타를 이용한 2차 배열 탐색

* N*N 배열에서 4방향의 인전 배열 요소를 탐색

* ```python
  lst = [[0]*N for _ in range(N)] # 오른쪽에서 시작해 시계방향으로 탐색하고 싶다면
  dy = [0, 1, 0, -1]
  dx = [1, 0, -1, 0] # 우측: A[i][j+1], 하: A[i+1][j], 좌측: A[i][j-1], 상: A[i-1][j] 
  for y in range(N):
      for x in range(N): # 좌표들에 대해서
          for k in range(4): # dy, dx를 이용해 주변 좌표 체크
              ny = y + dy[k]
              nx = x + dx[k]
              if N>ny>=0 and N>ny>=0: # 새로운 좌표가 유효한 좌표라면...
                  ...
  ```





### 전치 행렬

* 대각을 기준으로 대칭

* ```python
  for i in range(N):
      for j in range(N):
          if i < j: # 대각 기준 위쪽에서만
              lst[i], lst[j] = lst[j], lst[i]
  ```





## 비트 연산자를 이용한 부분집합 구하기

* 원소가 n 개 일때, 부분집합의 수는 2^n개

* 각각의 원소에 대해 0 또는 1로 포함관계를 표현해 부분집합을 생성할 수 있음

* ```python
  bit = [0, 0, 0, 0]
  for i in range(2):
      bit[0] = i
      for j in range(2):
          bit[1] = j
          for k in range(2):
              bit[2] = k
              for p in range(2):
          		bit[3] = p
  ```



### 비트 연산 연습

* 비트연산을 사용해서 표현할 수도 있음

* 비트 연산?

* ```python
  & # 비트 단위의 AND 연산
  | # 비트 단위의 or 연산
  << # 피연산자의 비트 열을 왼쪽으로 이동
  >> # 피연산자의 비트 열을 오른쪽으로 이동
  
  #ex
  1<<n # = 2^n / n이 5 라면: 00001 -> 10000(= 2^5)
  ```

* ```python
  lst = [1,2,3,4,5]
  n = len(lst)
  
  for i in range(1<<n): # 2^n 가지 경우의 수에 대해 (00000~11111)
      for j in range(n): # lst 의 자리수마다
          if i & (1<<j): # i의 각 자리가 부분집합에 포함인지 아닌지 검사
              print(arr[j], end = ', ')
      print()
  ```



## 검색

### 순차 검색

* 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용

* 구현이 쉽지만 검색 대상이 많은 경우 수행시간이 급격히 증가

* ```python
  while i<n and a[i]!=key:
  # 이렇게 리스트의 인덱스에 대한 검사 앞에 i에 대한 검사가 먼저 와야 인덱스 에러가 없음
  ```



### 이진 검색

* 정렬된 자료가 필요함 ***

* 자료의 가운데에 있는 항목의 키 값과 크기를 비교해 다음 검색의 범위를 결정

* 찾고자 하는 값을 찾을 때까지 반복

* ```python
  def binarySearch():
      start = 0
      end = n-1
      while start <= end:
          middle = (start + end)//2
          if lst[middle] == key:
              return True
          elif lst[middle] > key:
              end = middle - 1
          else:
              start = middle + 1
      return False
  ```

* 재귀 함수로도 구현할 수 있지만 굳이?



## 인덱스

### 선택 정렬

* 주어진 자료에서 가장 작은 값의 원소부터 차례대로 선택해 위치를 교환하는 방식

* O(n^2)의 시간 복잡도를 가짐

* ```python
  for i in range(N-1):
      minIdx = i
      for j in range(i+1, N):
          if lst[minIdx] > lst[j]: # 리스트의 최솟값 인덱스 찾기
              minIdx = j
      lst[i], lst[minIdx] = lst[minIdx], lst[i] # 찾은 최솟값을 검색 범위의 맨 앞으로
  ```

* k 번째로 작은 수를 찾는 경우, 굳이 끝까지 정렬하지 않아도 된다(k가 비교적 작을 때 유용)

* 교환의 횟수가 버블/ 삽입정렬보다 적다



# 연습

## 비트연산 이용한 부분집합 찾기

* ``` python
  T = int(input())
  
  for tc in range(1, T+1):
      lst = list(map(int, input().split()))
      n = len(lst)
      for i in range(1, 1<<n):
          tot = 0
          for j in range(n):
              if i & (1<<j):
                  tot += lst[j]
          if tot == 0:
              print(f'#{tc} 1')
              break
      else:
          print(f'#{tc} 0')
  ```

* 익숙하지 않아서 아직 사용법이 헷갈림, 특히 i j 등이 같이 사용되기 시작하면서



## 델타를 이용한 2차원배열 탐색

* ```python
  T = int(input())
  
  for tc in range(1, T+1):
      n = int(input())
      lst = [[0]*n for _ in range(n)]
  
      dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  
      x, y, dx, dy= 0, 0, 0, 0
      k = 0
  
      for i in range(1, n**2 + 1):
          nx = x+dx
          ny = y+dy
          if n > nx >= 0 and n > ny >= 0 and lst[ny][nx] == 0:
              x, y = nx, ny
          else:
              k = (k+1)%4
              dx, dy = dxy[k]
              x = x + dx
              y = y + dy
  
          dx, dy = dxy[k]
          lst[y][x] = i
  
      print(f'#{tc}')
      for j in range(n):
          print(*lst[j])
  ```

* 전에 한 번 풀었던 문제여서 다른 방법으로 풀어보려고 했음

* 마찬가지로, dx dy로 좌표를 움직여서 새로 선언하는곳에 실수가 있어서 한참 걸렸음

* 사용법에 익숙해지면 쓸곳이 있지 않을까?



* 원래 풀이

* ```python
  T = int(input())
   
  for idx in range(1, T+1):
      n = int(input())
   
      ans_lst = []
      for i in range(n):
          ans_lst.append([0 for j in range(n)]) # 2차원 배열 초기화
   
      num = 1 # 추가할거
      cnt = 0 # -1 에 제곱해서 방향바꿀거
      new_n = n # 2번 지나면 1씩 감소할거
      x = -1
      y = 0
      # 아마 여기 루프
      while 1:
          for i_1 in range(new_n):
              x += (1 * (-1)**cnt)
              ans_lst[y][x] = num
              num += 1
   
          new_n -= 1
   
          for i_2 in range(new_n):
              y += (1 * (-1)**cnt)
              ans_lst[y][x] = num
              num += 1
   
          if num > n**2:
              break
   
          cnt += 1
   
      print(f'#{idx}')
      for print_i in range(n):
          print(*ans_lst[print_i])
  ```

