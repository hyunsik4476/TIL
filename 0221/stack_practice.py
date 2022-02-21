T = int(input())

for tc in range(1, T+1):
    strs = list(input())
    N = len(strs)
    stack = []
    ans = 1
    for i in range(N):
        if strs[i] == '(':
            stack.append(1)
        elif strs[i] == ')':
            if stack:
                stack.pop()
            else:
                ans = 0
                break
    if stack:
        ans = 0

    if ans:
        print('True')
    else:
        print('False')
