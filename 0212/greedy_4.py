'''
어떤 수 N이 1이 될 때까지 N-1 혹은 N/K 중 하나의 연산을 한다
단, N/K는 N이 K로 나누어 떨어질 때만 실행할 수 있다
이 때 최소한의 연산 횟수를 구하자
'''

N, K = map(int, input().split())
ans = 0

while N != 1:
    remain = N % K
    if remain == 0:
        N //= K
        ans += 1
    else:
        N -= remain
        ans += remain

print(ans)