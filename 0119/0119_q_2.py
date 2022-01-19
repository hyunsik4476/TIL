def fn_test(x, y):
    z = x + y
    print(z)

result = fn_test(1, 3) # 이 지점에서 함수가 실행은 되므로 z값이 프린트는 됨
print(result) # 다만, 함수가 return 하는 값이 없으므로 result에는 None이 저장됨