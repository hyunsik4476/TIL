num = 5

for i in range(1, num + 1):
    print(i)

lst = list(range(3, 1, -1))
print(lst)

for i in range(num , -1, -1):
    print(i)

tot = 0
cnt = 0
for num in range(1, num + 1):
    tot += num
    cnt += 1
print(f'{tot} {cnt} {tot / cnt}')