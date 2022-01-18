import math

num_1 = 0.1 * 3
num_2 = 0.3
# if math.isclose(num_1, num_2):
#     print('num_1 = num_2')

if abs(num_1-num_2) < 1.e-10:
    print('num_1 = num_2')

a = 4
print(math.sqrt(a))