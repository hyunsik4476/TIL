def step_cnt(page, target):  # 찾을 숫자 받기
    tot = 1
    l = 1
    r = page
    mid_num = int((l + r) / 2)  # 중간 페이지

    while mid_num != target:  # 찾는 숫자와 같아질때까지
        if mid_num == page-1:  # pg 와 target 이 같은 경우 예외처리
            tot += 1
            break

        tot += 1
        if mid_num > target:
            r = mid_num

        elif mid_num < target:
            l = mid_num
        mid_num = int((l + r) / 2)

    return tot


T = int(input())

for tc in range(1, T+1):
    pg, A, B = map(int, input().split())
    step_A = step_cnt(pg, A)
    step_B = step_cnt(pg, B)

    if step_A < step_B:
        print(f'#{tc} A')
    elif step_A > step_B:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
