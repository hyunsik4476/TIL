alps = ['a', 'b', 'c', 'd']
strs_1 = ''.join(alps)

nums = [1, 2, 3, 4]
strs_2 = ''

list_1 = []

print(alps, strs_1)

for num in nums:
    # strs_2 = strs_2.join(num) #하나씩 추가하고 싶지만 정상작동 안함(반복가능한 객체가 아님)
    # print(strs_2)

    # list_1.append(str(num)) #타입 항상 주의
    # strs_2 = ''.join(list_1)
    # print(strs_2)
    
    strs_2 = strs_2 + '{0}'.format(num)
    print(strs_2)