T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    # 정렬하기
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    print(f'#{tc} ', end = '')
    for k in range(5):
        a = lst[-(k+1)]
        b = lst[k]
        print(a, b, end = ' ')
    print()