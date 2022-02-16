T = int(input())

for tc in range(1, T+1):
    tc_input = int(input().split()[1])
    str_lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    cnt = [0]*10

    input_str = input().split()
    for num_str in input_str:
        for i in range(10):
            if num_str == str_lst[i]:
                cnt[i] += 1

    ans = ''
    print(f'#{tc}')
    for j in range(10):
        print((str_lst[j] + ' ')*cnt[j], end = '')