# 저장 : 인접 리스트
arr = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = lst[i*2], lst[i*2 + 1]
    arr[n1].append(n2)
    arr[n2].append(n1)

# 저장 : 인접 행렬
for i in range(E):
    n1, n2 = lst[i*2], lst[i*2 + 1]
    arr[n1][n2] = 1
    arr[n2][n1] = 1

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