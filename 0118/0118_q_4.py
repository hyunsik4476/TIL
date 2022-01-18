number = int(input())
if number >= 0:
    aliq_lists = [num for num in range(1, number + 1) if number % num == 0]
else:
    aliq_lists = [num for num in range(number - 1, 0) if number % num == 0]

print(aliq_lists)