'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''


def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

V, E = map(int, input().split())
rep = [i for i in range(V+1)]
edge = []

for _ in range(E):
    u, v, weight = map(int, input().split())
    edge.append([weight, u, v])
edge.sort()

edge_cnt = 0
tot = 0
for w, u, v in edge:
    if find_set(v) != find_set(u):
        edge_cnt += 1
        union(v, u)
        tot += w
        if edge_cnt == V:
            break
print(tot)
