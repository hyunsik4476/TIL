'''
N개의 행, M개의 열을 가진 카드 더미가 주어짐 (M*N)
먼저 행을 선택하고 행에 포함된 카드 중 가장 숫자가 낮은 카드ㅡㄹ 뽑는다
'''
N, M = map(int, input().split())
lsts = [0]*N
for i in range(N):
    lsts[i] = list(map(int, input().split()))

ans = min(lsts[0])
for j in range(N):
    tmp = min(lsts[j])
    if tmp > ans:
        ans = tmp
print(ans)
