from pprint import pprint
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [[0]*10 for _ in range(10)]
    ans = 0

    for _ in range(N):
        x1, y1, x2, y2, c = map(int, input().split()) # 좌표 1, 좌표 2, 색(1 = 빨강, 2 = 파랑)
        for y in range(y1, y2+1):
            for x in range(x1, x2+1): # 인덱스 범위 조심
                lst[y][x] += 1
                if lst[y][x] >= 2: # 두 번 이상 체크된 곳(색이 겹친곳)
                    ans += 1 #에서 결과에 +1

    print(f'#{tc} {ans}')
