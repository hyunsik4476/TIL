numbers = [1, 3, 2, 5, 4, 6, 7]
tot = len(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# sorted_numbers = numbers.sort()
# print(sorted_numbers)
# print(numbers)

if tot % 2 == 0:
    print(sorted_numbers[tot//2 - 1], sorted_numbers[tot//2]) #tot//2 - 1 ???
else:
    print(sorted_numbers[tot//2])