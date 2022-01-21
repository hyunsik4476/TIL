'''
암거나 연습
조건문을 만들 때, 무엇과 비교해야 하는지 다시 한 번 더 생각해볼것
if lst[idx - 1] >= lst[idx]: 따위로 만들면 당연히 고장남
'''

input_str = '-1 -3 -2 -1 -5'
lst = list(map(int, input_str.split()))
print(lst)

if lst:
    max_num = lst[0]
    for idx in range(1, len(lst) + 1):
        if lst[idx - 1] >= max_num:
            max_num = lst[idx - 1]
    print(max_num)
else:
    print('빈 리스트 입니다.')