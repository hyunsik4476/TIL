def BFS(G, v):
    visited = [0]*(n+1)
    queue = []
    queue.append(v)             # 시작점을 큐에 넣음
    while queue:
        t = queue.pop(0)        # deQueue 부터 하는 것에 주의
        if not visited[t]:
            visited[t] = True
            print(t)
        for i in G[t]:          # t와 연결된 모든 정점 검사
            if not visited[i]:  # 방문한 적 없으면
                queue.append(i) # 큐에 추가


G = {
    1: [2, 3, 4],
    2: [1], 3: [1], 4: [1, 5, 6, 7],
    5: [4], 6: [4], 7: [4]
    }
n = 10
BFS(G, 1)