def stepcnt(page, target): # 찾을 숫자 받기
    tot = 1
    l = 1
    r = page
    mid_num = int((l + r) / 2) # 중간 페이지
    tmp_num = 1 if mid_num > target else page
    prev_mid = page if mid_num < target else 1

    while mid_num != target: # 찾는 숫자와 같아질때까지
        # print(target, mid_num, l, r)
        tot += 1
        if mid_num > target:
            l = tmp_num
            r = mid_num
            prev_mid = mid_num

        elif mid_num < target:
            l = mid_num
            r = prev_mid
            tmp_num = mid_num
        mid_num = int((l + r) / 2)

    return tot

T = int(input())

for tc in range(1, T+1):
    pg, A, B = map(int, input().split())
    step_A = stepcnt(pg, A)
    step_B = stepcnt(pg, B)
    print(step_A, step_B)