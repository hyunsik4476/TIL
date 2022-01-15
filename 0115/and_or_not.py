print(2 or 3) # 2
print(0 or 3) # 3

print(2 and 3) # 3
print(0 and 3) # 0

phone_book = {'햄버거': '1','치킨': '2', '피자': '3'}

for key, value in phone_book.items():
    if value == ('2' and '3'):
        print(key)
#피자

for key, value in phone_book.items():
    if value == ('2' or '3'):
        print(key)
#치킨

for key, value in phone_book.items():
    if value == '1' or value == '3':
        print(key)
#햄버거 피자

print(not 2)