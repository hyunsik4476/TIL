def f(i, N, K):     # i : 원소의 인덱스(tree의 단계)/ N : 전체 원소 수
                    # K : 찾는 합
    if i == N:      # 부분집합이 완성 (N개의 단계가 체크됨)
        s = 0
        for j in range(N):
            if bit[j] == 1:
                s += a[j]
        if s == K:
            for j in range(N):
                if bit[j]:
                    print(a[j], end = '')
            print()
        return
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

a = [1,2,3,4,5,6,7,8]
N = len(a)
bit = [0]*N
f(0, N, 10)