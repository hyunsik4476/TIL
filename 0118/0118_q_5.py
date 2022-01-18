numbers = [1, 4, 3, 2, 5, 6]
tot = len(numbers)

sorted_numbers = sorted(numbers)

if tot % 2 == 0:
    print(sorted_numbers[tot//2]) #tot//2 - 1 ???
else:
    print(sorted_numbers[tot//2])