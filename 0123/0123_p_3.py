A = 36912369
cnt = 0
if '3' in str(A) or '6' in str(A) or '9' in str(A):
    cnt += 1
print(cnt) # 1

cnt_2 = 0
for str_num in str(A):
    if '3' == str_num or '6' in str_num or '9' in str_num:
        cnt_2 += 1
print(cnt_2) # 6