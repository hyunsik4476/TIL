T = int(input())

for tc in range(1, T+1):
    strs = input()
    N = len(strs)
    stack = [0]*N       # 저장용 스택
    top = -1            # 현재 위치
    ans = 1             # 답 판별용 변수

    for i in range(N):  # 문자열 내의 모든 문자에 대해서
        if strs[i] == '(' or strs[i] == '{':    # 문자가 여는괄호면
            top += 1                            # 스택 포인터 이동 후
            stack[top] = strs[i]                # 해당 여는괄호 저장

        elif strs[i] ==')':                     # 닫는소괄호인 경우
            if stack[top] == '(':               # 마지막에 저장된 괄호가 여는소괄호면
                stack[top] = 0                  # 지우고
                top -= 1                        # 스택포인터 이동
            else:
                ans = 0                         # 마지막 저장된게 닫는소괄호가 아니면
                break                           # 답=0, 판별 종료

        elif strs[i] == '}':                    # 중괄호에 대해 같은 일 수행
            if stack[top] == '{':
                stack[top] = 0
                top -= 1
            else:
                ans = 0
                break

    if stack[top] != 0:                         # 끝까지 검사했을 때 스택에 괄호가 남아있으면
        ans = 0

    print(f'#{tc} {ans}')