T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 1
    max_cnt = 0
    for i in range(1, N):
        if lst[i] > lst[i-1]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= max_cnt:
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')