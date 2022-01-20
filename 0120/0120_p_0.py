def my_abs(x):
    if type(x) == complex:
        result = 0
        new_x = str(x)[:-1].replace('j', '')
        lst = []
        
        if '-' in new_x:
            new_x_split = new_x[1:].split('-')
            lst = list(map(int,filter(lambda x: x, new_x_split)))
        if '+' in new_x:
            new_x_split = new_x.split('+')
            lst = list(map(int,filter(lambda x: x, new_x_split)))
        else:
            lst = [0, int(new_x)]

        for num in lst:
            result += num ** 2

        return result ** 0.5
        
    elif x > 0:
        return x
    elif x < 0:
        return -x
    else:
        return 0

print(my_abs(+41231j))
print(my_abs(-0.0))
print(my_abs(-5))

# print(str(1+99j)[1:-1].replace('j', ''))
# print(str(1-99j)[:-1].replace('j', ''))
# print(str(-99j)[:-1].replace('j', '')) # -0-99
# print(str(+99j)[:].replace('j', '')) # 99
# print(str(+99j)[:-1].replace('j', '')) # 9
# print(str(0-99j)[:-1].replace('j', '')) # 99
# print(str(0-99j)[:].replace('j', '')) # -99

# print(list(map(int,filter(lambda x: x, ['', 3, '', '3']))))