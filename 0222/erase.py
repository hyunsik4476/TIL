T = int(input())

for tc in range(1, T+1):
    lst = list(input())
    N = len(lst)
    check = [0]*N   # 스택용 빈 통 만들기
    top = -1        # 스택의 현재 위치
    ans = 0         # 남은 글자의 수
    for i in range(N):
        if lst[i] != check[top]:    # 스택의 최상단 글자가 문자열과 다르면
            top += 1                # 다음 위치로
            ans += 1
            check[top] = lst[i]     # 스택에 추가
        else:                       # 스택의 최상단 글자가 문자열과 같으면
            check[top] = 0          # 최상단 문자 0으로 초기화
            top -= 1                # 현재 위치 -1
            ans -= 1
    print(f'#{tc} {ans}')