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