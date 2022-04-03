# 저장 1 : 부모 번호가 인덱스
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

for i in range(E):
    p, c = lst[2*i] , lst[2*i + 1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

# 저장 2 : 자식 번호가 인덱스
par = [0] *(V+1)
for i in range(E):
    p, c = lst[2*i], lst[2*i + 1]
    par[c] = p

# 루트 찾기
root = 0
for i in range(1, V+1):
    if par[i] == 0:
        root = i
        break

# 조상 찾기
anc = []
v = last
while v//2 != 0:
    anc.append(lst[v//2])
    v = v//2