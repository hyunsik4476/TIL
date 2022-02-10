# 1~ N 까지 상자 0 0 0 0 0 N 개
# Q회 동안 연속 상자를 동일 숫자로 변경
# i(1~Q) 번 작업에 대해 L번~R번 숫자를 i 로 변경
# tc/ N, Q/ Q개 줄에 걸쳐 L_i, R_i

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0]*N
    input_lst = [0]*Q
    for idx in range(Q):
        input_lst[idx] = map(int, input().split())
    for i in range(Q): # 주의 실제 i 는 1~ Q/ 여기서는 0~ Q-1 / L = 1은 i= 0부터 변경함
        L, R = input_lst[i]
        for j in range(R-L+1):
            box[L-1+j] = i+1
    print(f'#{tc} ', end='')
    print(*box)
