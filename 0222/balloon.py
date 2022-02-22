T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_tot = 0
    for y in range(N):
        for x in range(M):
            tot = arr[y][x]
            for k in range(1, arr[y][x]+1):
                for dy, dx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nx = x+dx*k
                    ny = y+dy*k
                    if M>nx>=0 and N>ny>=0:
                        tot += arr[ny][nx]
            if max_tot < tot:
                max_tot = tot
    print(f'#{tc} {max_tot}')