'''
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(stv, V):
    visited[stv] = 1
    print(stv)
    for w in range(1, V+1):
        if visited[w] == 0 and arr[stv][w] == 1:
            dfs(w, V)


V, E = map(int, input().split())
lst = list(map(int, input().split()))
arr = [[0]* (V+1) for _ in range(V+1)]

for i in range(E):
    n1, n2 = lst[i*2], lst[i*2 + 1]
    arr[n1][n2] = 1
    arr[n2][n1] = 1

visited = [0]*(V+1)
dfs(1, V)