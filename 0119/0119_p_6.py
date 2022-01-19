# 람다함수 w/ 필터
def odd(n):
    return n % 2 # ???

print(list(filter(odd, range(5))))

print(list(filter(lambda n: n % 2, range(5))))

print(list(filter(lambda n: n  if n % 2 == 1 else None, range(5))))