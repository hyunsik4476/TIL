num = 50

for i in range(1, num + 1):
    if not num % i:
        print(f'{i} ', sep = ',', end = '') # 콤마 못넣나?

lst = [i for i in range(1, num + 1) if not num % i]

print(pnum for pnum in lst)