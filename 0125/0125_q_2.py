def low_and_up(input_str):
    lst = [alp for alp in input_str]
    for i in range(len(lst)):
        if i % 2: # index 홀수
            lst[i] = lst[i].upper()
        else: # index 0, 짝수
            lst[i] = lst[i].lower()
    return ''.join(lst)

print(low_and_up('apple'))
print(low_and_up('banaNA'))

c = 'apple'
print(c[2].upper())