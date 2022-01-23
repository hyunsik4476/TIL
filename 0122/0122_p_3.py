inum = 5
lst = []
strs = ''

for num in range(1, inum + 1):
    lst.append(num)
    strs = strs + str(num) + ' '
    print(*lst)
    print(strs)

for alp in strs:
    print(alp) # 공백문자도 alp 하나로 취급돼서 10 줄 나옴