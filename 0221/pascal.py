from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1
    if N > 1:
        arr[1][0], arr[1][1] =1, 1

    print(f'#{tc}')
    for i in range(2, N):
        arr[i][0], arr[i][i] = 1, 1
        for x in range(1, i):
            arr[i][x] = arr[i-1][x-1]+arr[i-1][x]

    for j in range(N):
        for num in arr[j]:
            if num:
                print(num, end = ' ')
        print()