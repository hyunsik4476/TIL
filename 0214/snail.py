import pprint
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = [[0]*n for _ in range(n)]

    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    nx,ny= 0, 0
    k = 0
    lst[0][0] = 1

    for i in range(1, n**2):
        dx, dy = dxy[k]
        nx = nx+dx
        ny = ny+dy
        if n>nx>=0 and n>ny>=0 and lst[ny][nx] == 0:
            pass
        else:
            k = (k+1)%4
            nx = nx - dx
            ny = ny - dy
            dx, dy = dxy[k]
            nx = nx + dx
            ny = ny + dy

        lst[ny][nx] = i+1

    print(f'#{tc}')
    for j in range(n):
        print(*lst[j])