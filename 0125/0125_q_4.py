def alp_low(input_str):
    ans = ''
    for i in range(len(input_str)):
        ans += input_str[i].lower()
    print(ans)

alp_low('APPLE')