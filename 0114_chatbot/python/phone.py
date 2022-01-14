# 연락처 딕셔너리
phone_book = {'햄버거': '1234-1234','치킨': '1234-5678', '피자': '8765-4321'}


print(phone_book)
print(phone_book['햄버거'])
print([key for key, value in phone_book.items() if value == ('8765-4321')])