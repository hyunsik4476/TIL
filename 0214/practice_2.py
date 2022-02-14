T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    n = len(lst)
    for i in range(1, 1<<n):
        tot = 0
        for j in range(n):
            if i & (1<<j):
                tot += lst[j]
        if tot == 0:
            print(f'#{tc} 1')
            break
    else:
        print(f'#{tc} 0')
