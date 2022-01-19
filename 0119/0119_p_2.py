def ham():
    a = 'spam' # 로컬 변수
    return a

# 1.    
# print(a) # NameError

# 2.
# ham()
# print(a) # 여전히 NameError

# 블랙박스의 결과를 받아보고 싶으면 반환 값을 변수에 저장
# 결과를 주고 싶으면 return 할것

# 3.
a = ham() # 이 곳의 a
print(a) # 이 a 는