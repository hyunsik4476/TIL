T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split()) # 1회 충전 이동량/ 목적지 정류장/ 충전 정류장 수
    charge_idx = map(int, input().split())
    charge_lst = [0]*(N+1)
    for idx in charge_idx:
        charge_lst[idx] = 1

    ans = 0
    i = 0
    while 1:
        check = 0 # 일단 없다고 가정
        for j in range(1, K+1): # K칸 이동할 때
            if i+j >= N: # 도착하면
                check = 2
                break

            if charge_lst[i+j] == 1: # 충전소가 있으면
                check = 1 # 체크
                tmp_num = i+j # 다음 출발지점 후보

        if check == 0:
            ans = 0
            break
        if check == 2:
            break

        ans += 1
        i = tmp_num

    print(f'#{tc} {ans}')