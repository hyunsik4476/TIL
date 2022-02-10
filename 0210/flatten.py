T = 10

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    for _ in range(N):
        min_num, max_num = lst[0], lst[0]
        min_idx, max_idx = 0, 0
        for i in range(100):
            if lst[i] > max_num:
                max_idx = i
                max_num = lst[i]
            elif lst[i] < min_num:
                min_idx = i
                min_num = lst[i]

        if max_num - min_num <= 1:
            break

        lst[max_idx] -= 1
        lst[min_idx] += 1

        min_num, max_num = lst[0], lst[0]
        for i in range(100):
            if lst[i] > max_num:
                max_num = lst[i]
            elif lst[i] < min_num:
                min_num = lst[i]

    print(f'#{tc} {max_num-min_num}')