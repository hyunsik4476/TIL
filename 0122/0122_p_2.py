num = 50

for i in range(1, num + 1):
    if not num % i:
        print(f'{i} ', sep = ',', end = '') # 콤마 못넣나?

lst = [i for i in range(1, num + 1) if not num % i]

print(*lst, sep = ', ')
lst_2 = ['a', 'b', 'c', 'd', 'e']
for alp in lst_2:
    print(alp, end = ' ')
# for alp in *lst_2:
#     print(alp, end = ' ')