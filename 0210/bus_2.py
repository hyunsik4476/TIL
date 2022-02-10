'''
1~ 5000번 정류장이 있음
N개의 노선이 있고
i번째 노선은 A_i ~ B_i 까지를 모두 다님
P개의 정류장에 대해 각 정류장에 몇 개의 노선이 있는지 구하라
P이하의 입력은 정류장의 번호이다
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 노선의 수
    lst_1 = [0]*N # 노선의 정보
    for i in range(N):
        lst_1[i] = list(map(int, input().split()))

    P = int(input()) # 정류장의 수
    lst_2 = [0]*P # 확인할 정류장 번호
    for j in range(P):
        lst_2[j] = int(input())

    cnt = [0]*5000
    for lst in lst_1: # 노선 정보가 담긴 리스트에 대해서
        a, b = lst
        for distance in range(b-a+1): # 각 노선의 거리 / 1, 3일 때 0~ 2번 인덱스에 접근할 수 있게끔
            cnt[a-1+distance] += 1

    print(f'#{tc} ', end='')
    for idx in lst_2: # 정류장 번호들에 대해서
        print(cnt[idx-1], end=' ')
    print()