T = int(input())

lst = [i+1 for i in range(12)]
for tc in range(1, T+1):
    N, K = map(int, input().split()) # 부분집합 원소의 수, 원소의 합
    ans = 0

    for i in range(1<<12): # 경우의 수
        tot = 0
        cnt = 0
        for j in range(12):
            if i & (1<<j):
                tot += lst[j] # 10101... 에서 1을 인덱스로 갖는 수의 합
                cnt += 1 # 원소의 수 체크용

            if cnt > N or tot > K: # 조건 초과 시
                break

        if tot == K and cnt == N: # 조건에 부합하면 답 + 1
            ans += 1

    print(f'#{tc} {ans}')