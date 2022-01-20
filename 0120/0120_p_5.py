def sum_of_digit(number):
    total = 0
    numbers = map(int, str(number))
    for number in numbers:
        total += number
    return total


print(sum_of_digit(1234))
print(sum_of_digit(4321))