'''
주어진 N개의 숫자를 M번 더해 가장 크게 만들 수 있는 해
단, 하나의 인덱스에 있는 숫자가 K번 초과해서 연속으로 사용될 수 없다
'''

N, M ,K = map(int, input().split())
data = list(map(int, input().split()))
ans = 0

data.sort()
max_1 = data[-1] # 가장 큰 수
max_2 = data[-2] # 두번째로 큰 수

# m1+m1+m1+m2+m1+m1 처럼 될 수 있다

i = 0
while 1:
    for _ in range(K):
        if i == M:
            break
        ans += max_1
        i += 1

    if i == M:
        break
    ans += max_2
    i += 1

print(ans)