T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 데이터의 가로, 세로

    lst = [list(map(int, input().split())) for _ in range(N)]
    sum_x = 0
    sum_y = 0
    sum_max = 0

    for y in range(N):
        for x in range(M):
            sum_x = (sum_x + lst[y][x]) * lst[y][x]  # 가로 연속된 1 합
            if sum_x > sum_max:
                sum_max = sum_x

    for x in range(M):
        for y in range(N):
            sum_y = (sum_y + lst[y][x]) * lst[y][x]  # 세로 연속된 1 합
            if sum_y > sum_max:
                sum_max = sum_y

    print(f'#{tc} {sum_max}')