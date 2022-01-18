number = int(input())
ans = ''

for num in range(1, number + 1):
    ans = ans + '{0} '.format(num)
    print(ans)