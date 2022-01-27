import math

def fee(minute, distance):
    m = minute
    d= distance

    f_1 = m/10 * 1200
    f_2 = math.ceil(m/30) * 525
    if d > 100:
        f_3 = 100 * 170 + (d - 100) * 85
    else:
        f_3 = d * 170
    
    return math.ceil(f_1 + f_2 + f_3)

print(fee(600, 50))
print(fee(600, 110))