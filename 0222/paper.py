def facto(n):       # 팩토리얼 함수
    if n == 1:
        return 1
    if memo[n] == 0:
        memo[n] = n*facto(n-1)  # 연습
    return memo[n]


T = int(input())
N_max = 30
memo = [0]*(N_max+1)            # 메모 저장
memo[0] = 1

for tc in range(1, T+1):
    N = int(input())
    a_max = N//10//2            # 큰 사각형의 가능한 최댓값
    ans = 0                     # 경우의 수의 총합
    for a in range(a_max+1):    # 모든 가능한 큰 사각형 갯수
        b = N//10 - a*2         # 각 경우에 작은 사각형 갯수
        ans += (facto(a+b)//(facto(a)*facto(b)))*(2**a)     # 에서 나올 수 있는 경우의 수 누적

    print(f'#{tc} {ans}')
