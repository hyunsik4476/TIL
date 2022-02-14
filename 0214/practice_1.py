T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [0]*N
    for i in range(N):
        lst[i] = list(map(int, input().split()))
    ans = 0

    for y in range(N):
        for x in range(N):
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_y = y - dy
                new_x = x - dx
                if N>new_y>=0 and N>new_x>=0:
                    ans += abs(lst[new_y][new_x] - lst[y][x])

    print(f'#{tc} {ans}')