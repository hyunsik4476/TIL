def f(i, N):
    if i == N:  # 순열 완성
        print(p)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[i], p[j] = p[j], p[i]
    return

p = [1,2,3]
N = len(p)
f(0, N)