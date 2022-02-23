def f(i, N, K):
    if i == N:  #한 개의 부분집합이 완성
        s = 0
        for j in range(N):
            if bit[j] == 1:
                s += a[j]
        if s == K:
            for j in range(N):
                if bit[j] == 1:
                    print(a[j], end = ' ')
            print()
        return
    else:
        bit[i] = 1
        f(i+1, N, K)
        bit[i] = 0
        f(i+1, N, K)


N = 10
a = [x for x in range(1, N+1)]
bit = [0]*(N)
K = 12
f(0, N, K)