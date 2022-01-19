def list_sum(input_list):
    total = 0

    for num in input_list:
        total += num

    return total

ans = list_sum([1, 2, 3, 4, 5])
print(ans)