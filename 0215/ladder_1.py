from pprint import pprint

T = 10

for tc in range(1, T+1):
    N = int(input())
    lst = [[0]+list(map(int, input().split()))+[0] for _ in range(100)] # 나중에 인덱스 넘버 - 1 해줄것

    for i in range(50): # 0 ~ 49 (즉, 절반)
        lst[i], lst[99-i] = lst[99-i], lst[i]  # 위아래 뒤집기

    x = lst[0].index(2) # 시작점 저장
    y = 0

    dxy = [[0, 1], [-1, 0], [1, 0]]  # k = 0, 1, 2 =아래, 좌, 우좌표 이동
    k = 0

    while 1:
        dx, dy = dxy[k]
        if k == 0: # 내려가던 중 갈림길 만나면
            if lst[y][x-1] == 1:  # 왼쪽으로 갈 수 있으면
                k = 1
                dx, dy = dxy[k]
            if lst[y][x+1]:     # 오른쪽으로 갈 수 있으면
                k = 2
                dx, dy = dxy[k]
        x, y = x+dx, y+dy # 일단 이동시킴(좌, 우 안만나면 아래로 감)
        
        if k == 1 or k == 2: # 왼쪽 혹은 오른쪽으로 이동중이라면, 
            if lst[y+1][x] == 1: # 내려갈 수 있으면
                k = 0
                dx, dy = dxy[k] # 방향 바꿈
                x, y = x+dx, y+dy # 일단 한칸 내려가기

        if y == 99:
            lst[y][x] = 3
            break

    a = lst[99].index(3)
    print(f'#{tc} {a-1}')