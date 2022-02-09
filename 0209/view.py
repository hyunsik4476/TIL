T = 10

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    i = 2
    view = 0

    for i in range(2, N-2):
        tmp_lst = [lst[i] - lst[i - 1], lst[i] - lst[i - 2], lst[i] - lst[i + 1], lst[i] - lst[i + 2]]
        min_num = tmp_lst[0]
        if lst[i]-lst[i - 1] > 0 and lst[i]-lst[i - 2] > 0:
            if lst[i] - lst[i + 1] > 0 and lst[i] - lst[i + 2] > 0:
                for num in tmp_lst:
                    if num < min_num:
                        min_num = num
                view += min_num

    print(f'#{tc} {view}')
