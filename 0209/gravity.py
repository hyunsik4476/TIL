T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = [0]*N

    for i in range(N-1):
        for j in range(i+1, N):
            if lst[i] > lst[j]:
                cnt[i] += 1

    maxV = cnt[0]
    for i in range(1, N):
        if cnt[i] > maxV:
            maxV = cnt[i]

    print(f'#{tc} {maxV}')
