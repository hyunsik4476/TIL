'''
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(stv, V):
    q = []
    q.append(stv)
    visited = [0] * (V + 1)
    visited[stv] = 1

    while q:
        tmpV = q.pop(0)
        print(tmpV)
        for w in arr[tmpV]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[tmpV] + 1


V, E = map(int, input().split())
lst = list(map(int, input().split()))
arr = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = lst[i*2], lst[i*2 + 1]
    arr[n1].append(n2)
    arr[n2].append(n1)

bfs(1, V)
