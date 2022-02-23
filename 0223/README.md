# APS_stack

> 20220223

## DFS

* 한 방향으로 깊이 탐색해 가다가 막다른 길일 경우 마지막 갈림길로 돌아와 다른 방향 탐색

* 스택 혹은 재귀로 구현 가능

* 방문한 노드를 스택에 저장해 가며 체크

* ```python
  def f(i, N, K):
      if i == N:  #한 개의 부분집합이 완성
          s = 0
          for j in range(N):
              if bit[j] == 1:
                  s += a[j]
          if s == K:
              for j in range(N):
                  if bit[j] == 1:
                      print(a[j], end = ' ')
              print()
          return
      else:
          bit[i] = 1
          f(i+1, N, K)
          bit[i] = 0
          f(i+1, N, K)
  
  
  N = 10
  a = [x for x in range(1, N+1)]
  bit = [0]*(N)
  K = 12
  f(0, N, K)
  ```





## 계산기

* 중위 표기법의 수식을 후위표기법으로 변경 (연산자를 피연산자 뒤에 표기)
* -> 각 연산자에 대해서 우선순위에 따라 다시 표시(괄호와 스택 사용)
* 후위 표기법의 수식을 스택을 이용해 계산



## 백트랙킹

* 해를 찾는 도중에 막히면 되돌아가서 다시 해를 찾아가는 방법
* 어떤 노드의 유망성을 점검 후, 유망하지 않다면 노드의 부모로 되돌아감
* `function(idx, N, targetsum, sum)` 과 같은 형태



### 부분합

* ```python
  def f(i, N, K, S): 	# S : i-1 까지 고려한 합
      if S == K:		# 강한 조건부터
          for j in range(N)
              if bit[j]:
                  print(a[j], end=' ')
          print()
      elif i == N:  	# 모든 원소에 대한 고려가 끝났으나 조건에 일치하지 않음
          return
      elif S > K:		# 이후의 원소에 대해 고려할 필요 없는 경우
          return
      
      else:			# 비트를 만드는 과정
          bit[i] = 1
          f(i+1, N, K, S+a[i])
          bit[i] = 0
          f(i+1, N, K, S) # 중요
      return
  
  N = 10
  a = [x for x in range(1, N+1)]
  bit = [0]*(N)
  K = 12
  f(0, N, K, 0)
  ```

* 같은 작업을 해도 함수의 호출 횟수를 줄일 수 있음

* 남은 구간의 합(RS)을 이용해 호출 횟수를 더 줄일 수 있음

* ```python
  def f(i, N, K, S, RS): # S : i-1 까지 고려한 합
      if S == K:
          for j in range(N)
              if bit[j]:
                  print(a[j], end=' ')
          print()
  
      elif i == N:  #한 개의 부분집합이 완성
          return
      elif S > K:
          return
      elif S + RS < K:	# S까지의 합과 그 이후의 합을 더했을 때 목표에 도달 못하면
          return
      else:
          bit[i] = 1
          f(i+1, N, K, S+a[i], RS-a[i])
          bit[i] = 0
          f(i+1, N, K, S, RS-a[i])
      return
  
  N = 10
  a = [x for x in range(1, N+1)]
  bit = [0]*(N)
  K = 12
  f(0, N, K, 0, sum(a))
  ```



### 순열

* 단계마다 사용 가능한 숫자 중 하나를 골라 넣음

* 혹은, 숫자 간 자리를 바꿔가며 하나씩 완성시키기

* ```python
  def f(i, N):
      if i == N:  # 순열 완성
          return
      else:
          for j in range(1, N):
              p[i], p[j] = p[j], p[i]
              f(i+1, N)
              p[i], p[j] = p[j], p[i]
  
  
  p = [1,2,3]
  N = len(p)
  f(0, N)
  ```

* 이렇게 만든 순열로 완전탐색에 사용 가능



## 분할 정복 알고리즘

* C^8 -> (C^4 ) * (C^4)
* 8번의 계산에서 5번으로 줄일 수 있음
* O(log_2 n) 의 시간 복잡도



### 퀵 정렬

* 합병정렬(merge sort) 와 다른 점은 퀵 정렬은 기준 아이템 중심으로 작은 것은 왼편, 큰 것은 오른편에 정렬

* 합병정렬과 다르게 퀵 정렬은 나눈 배열을 합치는 후처리 과정이 필요 없음

* 최악의 경우 O(n^2) 의 시간 복잡도

* 평균 복잡도가 O(nlogn)

* ```python
  def quickSort(a, begin, end):
      if begin < end: # 정렬할 대상이 남아있으면
          p = partition(a, begin, end)    # 피봇의 위치를 정하는 파티셔닝
          quickSort(a, begin, p-1)        # 피봇 기준 좌, 우에 반복
          quickSort(a, p+1, end)
  
  
  def partition(a, begin, end):   # (피봇 : 정렬 전 후 움직이지 않는 값) 찾기
      pivot = (begin + end) // 2  # 일단 하나 찍어서 피봇으로 정함
      L = begin       # 오른쪽으로 이동하면서 피봇 이상의 원소 찾기
      R = end         # 왼쪽으로 이동하면서 피봇 미만의 원소 찾기
      while L < R:    # L 과 R이 만날 때까지
          while L < R and a[L] < a[pivot]:
              L += 1
          while L < R and a[R] >= a[pivot]:
              R -= 1
          if L < R:   # 만나지 못하고 포인터가 멈추면 a[L]과 a[R]이 교환됨
              if L == pivot:
                  pivot = R
              a[L], a[R] = a[R], a[L]
      # L과 R이 만나면, while이 종료
      a[pivot], a[R] = a[R], a[pivot]
      return R        # 피봇의 위치 리턴
  
  ```



## 그래프

* 인접 행렬의 입력 받기???

* ```python
  '''
  정점의 갯수 V, 간선의 갯수 E
  3 2
  1 3 2 3
  '''
  
  V, E = map(int, input().split())
  arr = list(map(int, input().split()))
  
  # 인접 행렬 만들기 : 마지막 정점 번호를 인덱스로 갖는 2차원 배열
  adj = [[0]*(V+1) for _ in range(V+1)]
  
  for i in range(E):      # 간선의 갯수만큼
      n1, n2 = arr[i*2], arr[i*2 + 1]
      adj[n1][n2] = 1     # n1 과 n2 는 인접
      adj[n1][n2] = 1     # 방향 표시가 없는 경우 해야함
  
  # 인접 리스트 만들기
  adjList = [[] for _ in range(V+1)]
  
  for i in range(E):      # 간선의 갯수만큼
      n1, n2 = arr[i*2], arr[i*2 + 1]
      adjList[n1].append(n2)
      adjList[n2].append(n1)
  
  ```

