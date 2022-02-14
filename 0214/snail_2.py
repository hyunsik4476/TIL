import pprint
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = [[0]*n for _ in range(n)]

    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    x, y, dx, dy= 0, 0, 0, 0
    k = 0

    for i in range(1, n**2 + 1):
        nx = x+dx
        ny = y+dy
        if n > nx >= 0 and n > ny >= 0 and lst[ny][nx] == 0:
            x, y = nx, ny
        else:
            k = (k+1)%4
            dx, dy = dxy[k]
            x = x + dx
            y = y + dy

        dx, dy = dxy[k]
        lst[y][x] = i

    print(f'#{tc}')
    for j in range(n):
        print(*lst[j])