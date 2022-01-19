# 람다함수 w/ 필터
def odd(n):
    return n % 2 # ???

print(list(filter(odd, range(5))))
# 이게 왜 작동하나?
# 첫 추측: return 1 = n, return 0 =None ???
# print(odd(n)) 으로 확인해봄 -> 아님
# 해결: filter 함수에서 function 은 T/ F 판단

print(list(filter(lambda n: n % 2, range(5))))

print(list(filter(lambda n: n  if n % 2 == 1 else None, range(5))))
# 실상 이럴 필요가 없었음: n % 2 == 1 자체가 T/ F 를 반환하므로
# n 을 리턴하는 것에 대해: filter 함수의 동작에 대한 이해 부족