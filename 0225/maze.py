def bfs(x, y, N):
    visited = [[0]*N for _ in range(N)]
    queue = []
    queue.append((x, y))
    visited[y][x] = 1

    while queue:
        x, y = queue.pop(0)
        if arr[y][x] == 3:
            return visited[y][x] - 2    # 거쳐가는 칸 수
        for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and arr[ny][nx]!=1 and visited[ny][nx]==0:
                queue.append((nx, ny))
                visited[ny][nx] = visited[y][x] + 1
    return 0

T = int(input())

for tc in range(1, T+1):
    ans = 0
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]   # 미로
    check = [[0]*N for _ in range(N)]                   # 갔던 길 체크용

    for s_y in range(N):                                # 시작점 찾기
        for s_x in range(N):
            if arr[s_y][s_x] == 2:
                start_y = s_y
                start_x = s_x
    a = bfs(start_x, start_y, N)
    print(f'#{tc} {ans}')
    print(a)