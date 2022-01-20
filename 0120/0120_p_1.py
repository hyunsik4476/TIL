def my_abs(x):
    if type(x) == complex and x**2 < 0:
        new_x = str(x)[1:-1].replace('j', '')
        if '+' in str(x):
            a, b = map(int, new_x.split('+'))
        else:
            a, b = map(int, new_x.split('-'))
        return (a**2 + b**2)**0.5
        
    elif x > 0:
        return x
    elif x < 0:
        return -x
    else:
        return 0

print(my_abs(-41231j))
print(my_abs(-0.0))
print(my_abs(-5))
