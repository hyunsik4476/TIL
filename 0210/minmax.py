T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_num = lst[0]
    min_num = lst[0]

    for i in range(1, N):
        if lst[i] > max_num:
            max_num = lst[i]
        elif lst[i] < min_num:
            min_num = lst[i]

    print(f'#{tc} {max_num-min_num}')
