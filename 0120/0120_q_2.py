def get_secret_number(strs):
    ans = 0
    for str in strs:
        ans += ord(str) # chr(), ord()
    print(ans)
    return ans # 문제 조건을 잘 확인할 것

get_secret_number('tom')