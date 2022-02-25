# APS_queue

> 20220225

## 큐

### 큐의 특성

* 스택과 마찬가지로 삽입과 삭제 위치가 제한적
* 선입선출(머리: 첫 번째 원소or 삭제된 위치/ 꼬리: 저장된 원소 중 마지막 원소)
* enQuere/ deQueue



### 큐의 연산

1. 큐 생성 (front = rear = -1)
2. 원소 삽입(front = 그대로, rear += 1)
3. 원소 삭제(front += 1, rear = 그대로)
4. `if front == rear :` 비어있는 큐
5. `rear == n-1` 포화된 큐



## 선형 큐

### 선형 큐의 구현

```python
def enQueue(item):	# 삽입
    global rear
    if isFull() : print('queue_full')
    else:
        rear += 1
        Q[rear] = item

def deQueue():		# 삭제
    if isEmpty() : print('queue_empty')
    else:
        front += 1
        return Q[front]

def isEmpty():
    return front == rear

def isFull():
    return rear == len(Q) - 1

def Qpeek():		# 검색
    if isEmpty() : print('queue_empty')
    else: return Q[front+1]

Q = [0]*10
front = rear = -1
```



### 선형 큐 이용시 주의점

* 원소의 삽입/ 삭제를 반복할 경우, 배열의 앞 부분에 활용 가능한 공간이 있음에도
  포화상태로 인식할 가능성이 있음
* 논리적으로 배열의 처음과끝이 연결된 원형 큐 사용시 해결 가능



## 원형 큐

### 원형 큐의 구조

* front = rear = 0
* 인덱스가 n-1을 가리킨 후, 0으로 이동해야함
* 나머지 연산자 활용



### 원형 큐의 구현

```python
def enQueue(item):
    global rear
    if (rear+1) % len(cQ) == front: # 꼬리의 다음칸이 머리면 포화
        print('queue_full')
    else:
        rear = (rear+1) % len(cQ)
        cQ[rear] = item

def deQueue():
    if front == rear: 
        print('queue_empty')
    else:
        front = (front+1) % len(cQ)
        return cQ[front]        

cQ = [0]*10
front = rear = 0
```



## 우선순위 큐

### 우선순위 큐의 특성

* 우선순위를 가진 항목들을 저장함
* 선입선출이 아닌 우선순위가 높은 순서대로 나가게 됨



## 큐의 활용

### 버퍼

* 데이터를 전송하는 동안 일시적으로 데이터를 보관하는 영역
* 일반적으로 입출력/ 네트워크와 관련된 기능에 이용된다



## BFS

#### 방법 1

```python
def BFS(G, v):
    visited = [0]*(n+1)
    queue = []
    queue.append(v)             # 시작점을 큐에 넣음
    while queue:
        t = queue.pop(0)        # deQueue 부터 하는 것에 주의
        if not visited[t]:
            visited[t] = True
            print(t) 			# 노드에 방문해서 할 일
        for i in G[t]:          # t와 연결된 모든 정점 검사
            if not visited[i]:  # 방문한 적 없으면
                queue.append(i) # 큐에 추가
```

* 탐색 시작점의 인접 정점을 모두 방문하고 방문했던 정점을 시작점으로 하여 다시 검사
* visited 공간에 중복이 있을 수 있어 특정하기 어려움



#### 방법 2

```python
def BFS(G, v):
    visited = [0]*(n+1)         # 노드가 줄 선 적 있으면 1
    queue = []
    queue.append(v)             # 시작점을 큐에 넣음
    visited[v] = 1              # 줄 세운 정보 저장

    while queue:
        t = queue.pop(0)        # deQueue 부터 하는 것에 주의
        # 너비우선탐색의 목적 (뭐던간에)
        print(f' 노드 번호: {t}, 노드의 깊이: {visited[t]}')

        for i in G[t]:          # t와 연결된 모든 정점에 대해 줄선적 없으면
            if not visited[i]:
                queue.append(i)                 # 큐에 줄세우고
                visited[i] = visited[t] + 1     # 줄 섰던 정보 가공(이 경우 노드의 깊이)


G = {
    1: [2, 3, 4],
    2: [1], 3: [1], 4: [1, 5, 6, 7],
    5: [4], 6: [4], 7: [4]
    }
n = len(G)
BFS(G, 1)
```

* queue에 들어간 적 있는지에 대한 정보를 저장하는 방식
* 정점 갯수만큼의 visited 공간만 필요
