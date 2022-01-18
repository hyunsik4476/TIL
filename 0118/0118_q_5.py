numbers = [
82, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
]
tot = len(numbers)

sorted_numbers = sorted(numbers)


if tot % 2 == 0:
    print(sorted_numbers[tot//2 - 1], sorted_numbers[tot//2]) #tot//2 - 1 ???
else:
    print(sorted_numbers[tot//2])