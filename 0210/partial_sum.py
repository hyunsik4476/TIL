T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    tmp_lst = lst[:M]
    tmp_sum = 0

    for num in tmp_lst:
        tmp_sum += num

    max_ans = tmp_sum
    min_ans = tmp_sum

    for i in range(N+1-M):
        new_lst = lst[i: i+M]
        partial_sum = 0

        for num in new_lst:
            partial_sum += num

        if partial_sum > max_ans:
            max_ans = partial_sum
        elif partial_sum < min_ans:
            min_ans = partial_sum

    print(f'#{tc} {max_ans-min_ans}')