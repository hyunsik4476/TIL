T = int(input())

for tc in range(1, T+1):
    num = int(input())
    cnt = [0]*5
    i = 0
    # 2 3 5 7 11

    for prime in [2, 3, 5, 7, 11]:
        while num % prime == 0:
            num //= prime
            cnt[i] += 1
        i += 1

    print(f'#{tc} ', end='')
    print(*cnt)