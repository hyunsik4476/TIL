p = 1
q = []
N = 20
tot = 0
cnt = [0]*(N+1)
p_tot = [0]*(N+1)

while tot < N:
    q.append(p)
    cnt[p] += 1

    t = q.pop(0)
    p_tot[t] += cnt[t]
    tot += cnt[t]

    q.append(t)
    cnt[t] += 1
    p += 1
print(t)