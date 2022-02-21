T = int(input())

for tc in range(1, T+1):
    strs = list(input())
    N = len(strs)
    stack = [0]*1000
    top = -1
    ans = 1

    for i in range(N):
        if strs[i] == '(':
            top += 1
            stack[top] = strs[i]
        elif strs[i] == ')':
            if top == -1:
                ans = 0
                break
            else:
                top -= 1

    if top != -1:
        ans = 0

    if ans:
        print('True')
    else:
        print('False')