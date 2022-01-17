x, *y = [1, 2, 3, 4]
print(f'x, y = {x}, {y}') #x, y = 1, [2, 3, 4]
print('==================')
# x, *y, *z = [1, 2, 3, 4] #동작 안함
# print(f'x, y = {x}, {y}')

nums = [1, 2, 3, 4]
strs = 'hello'
print(*nums)
print(*strs)
print('==================')

div_result = divmod(5,2)
print(div_result, type(div_result)) # (2, 1) <class 'tuple'>
print('==================')

strs = 'hello'
strs_slicing = strs[::-1]
print(strs_slicing, type(strs_slicing)) # olleh <class 'str'>
print(strs[:10]) #왜?
#print(strs[:10][7]) #인덱스에러
print(strs[-4::]) #ello
print(strs[:-3:]) #he