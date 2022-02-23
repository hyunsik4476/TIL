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
