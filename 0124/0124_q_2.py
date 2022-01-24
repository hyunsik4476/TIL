a = ' apple banana juice '
print(a.find('b'))
print(a.find('A'))

lst_1 = a.split()
lst_2 = a.split('j')
print(lst_1) # ['apple', 'banana', 'juice']
print(lst_2) # [' apple banana ', 'uice ']

a_1 = a.replace('a', 'z', 3)
print(a)
print(a_1) # 맨 끝 count 수 만큼 a 가 z로 변경(미입력이 모든 a가 변경)

a_2 = a.strip() # 공백문자 제거
a_3 = a.strip('a')
a_4 = a.strip(' a')
print(a_2) # 'apple banana juice'
print(a_3) # ' apple banana juice '
print(a_4) # 'pple banana juice '

b = ''.join('HELLo')
b_1 = '!'.join('HELLo')
b_2 = '!'.join(['h', 'e', 'l', 'l', 'o'])
print(b)
print(b_1)
print(b_2)