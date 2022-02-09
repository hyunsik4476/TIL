T = int(input())

for tc in range(1, T+1):
    num = int(input())
    cnt = [0]*12
    t, r, i = 0, 0, 0

    while num:
        cnt[num % 10] += 1
        num //= 10

    while i < 10:
        if cnt[i] >= 3:
            cnt[i] -= 3
            t += 1
            continue

        if cnt[i] and cnt[i+1] and cnt[i+2]:
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            r += 1
            continue

        i += 1

    if t + r == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')