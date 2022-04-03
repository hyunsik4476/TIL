# 내용 정리

## 트리

### 저장

* 부모 번호를 인덱스로 저장

* ```python
  ch1 = [0] * (V+1)
  ch2 = [0] * (V+1)
  
  for i in range(E):
      p, c = lst[2*i] , lst[2*i + 1]
      if ch1[p] == 0:
          ch1[p] = c
      else:
          ch2[p] = c
  ```



* 자식 번호를 인덱스로 저장

* ```python
  par = [0] *(V+1)
  for i in range(E):
      p, c = lst[2*i], lst[2*i + 1]
      par[c] = p
  ```



### 탐색

* 루트 찾기

* ```python
  root = 0
  for i in range(1, V+1):
      if par[i] == 0:
          root = i
          break
  ```



* 조상 찾기

* ```python
  anc = []
  v = last
  while v//2 != 0:
      anc.append(lst[v//2])
      v = v//2
  ```



### 삽입

* 라스트에 원소 삽입 후 조건에 맞을 때까지 위치 변환

* 힙에 원소 삽입하는 방법 :

* ```python
  def enq(n):
      global last
      last += 1
      tree[last] = n
      c = last
      p = c//2
      while p >= 1 and tree[p] < tree[c]:
          tree[p], tree[c] = tree[c], tree[p]
          c = p
          p = c // 2
  ```



### 삭제

* 트리에서 원소 삭제는 루트만 가능

* 힙에서 원소 삭제하기 :

* ```python
  def deq():  # 삭제과정 : 루트 삭제 -> 마지막 정점 값을 루트로 -> 교환 시작
      global last
      tmp = tree[1]
      tree[1] = tree[last]
      last -= 1
      p = 1
      c = p * 2
  
      while c <= last:
          if c+1 <= last and tree[c] < tree[c+1]:
              c += 1
          if tree[p] < tree[c]:
              tree[p], tree[c] = tree[c], tree[p]
              p = c
              c = p * 2
          else:
              break
  
      return tmp
  ```



## 정렬

### 퀵소트

* 부동점 s 를 찾고 그 부동점의 좌 우에 대해 다시 부동점을 찾아나감

  * 길이가 1이 될때까지

* 부동점 찾기

* ```python
  def partition(A, l, r):
      pivot = A[l]
      i, j = l, r
      while i <= j:
          while i <= j and A[i] <= pivot:
              i += 1
          while i <= j and A[j] >= pivot:
              j -= 1
          if i < j:
              A[i], A[j] = A[j], A[i]
      A[l], A[j] = A[j], A[l]
      print(f'pivot: {pivot}, s: {j}')
      return j
  ```



### 머지소트

* 리스트 길이가 1이 될때까지 반으로 나누기

* 마지막에 머지함수를 통해 하나로 합치는걸 반복

* ```python
  def merge_sort(A):
      if len(A) <= 1:
          return A
  
      mid = len(A)//2
      left_lst = [0]* mid
      right_lst = [0] * (len(A) - mid)
  
      for i in range(mid):
          left_lst[i] = A[i]
      for j in range(mid, len(A)):
          right_lst[j - mid] = A[j]
      left_lst = merge_sort(left_lst)
      right_lst = merge_sort(right_lst)
  
      return merge(left_lst, right_lst)
  ```



## 그래프

### 저장

* 인접 리스트

* ```python
  arr = [[] for _ in range(V+1)]
  for i in range(E):
      n1, n2 = lst[i*2], lst[i*2 + 1]
      arr[n1].append(n2)
      arr[n2].append(n1)
  ```



* 인접 행렬

* ```python
  for i in range(E):
      n1, n2 = lst[i*2], lst[i*2 + 1]
      arr[n1][n2] = 1
      arr[n2][n1] = 1
  ```



### 탐색

* dfs 혹은 bfs 를 사용해 탐색 가능

* ```python
  # 인접 리스트 탐색 (bfs)
  def bfs(stv, V):
      q = []
      q.append(stv)
      visited = [0]*(V+1)
      visited[stv] = 1
      while q:
          tmpV = q.pop(0)
          for w in arr[tmpV]:
              if visited[w] == 0:
                  q.append(w)
                  visited[w] = 1
  
  # 인접 행렬 탐색 (dfs)
  def dfs(stv, V):
      visited[stv] = 1
      print(stv)
      for w in range(1, V+1):
          if visited[w] == 0 and arr[stv][w] == 1:
              dfs(w, V)
  ```

