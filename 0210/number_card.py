T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input()))
    cnt = [0]*10

    for i in range(N):
        cnt[lst[i]] += 1

    max_num = 0
    max_cnt = cnt[0]
    for j in range(10):
        if cnt[j] >= max_cnt:
            max_cnt = cnt[j]
            max_num = j

    print(f'#{tc} {max_num} {max_cnt}')
