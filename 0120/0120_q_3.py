def get_secret_number(strs_1, strs_2):
    ans_1 = 0
    ans_2 = 0

    for str in strs_1:
        ans_1 += ord(str) # chr(), ord()
    for str in strs_2:
        ans_2 += ord(str)

    if ans_1 > ans_2:
        return strs_1
    else:
        return strs_2

get_secret_number('z', 'a')
get_secret_number('tom', 'jhon')