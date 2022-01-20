def get_secret_word(params: list):
    ans = ''
    for num in params:
        ans += chr(num) # chr(), ord()
    return ans # 문제 조건을 잘 확인할 것

get_secret_word([83, 115, 65, 102, 89])