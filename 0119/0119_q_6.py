def all_list_sum(input_lists):
    total = 0

    for lists in input_lists:
        for num in lists:
            total += num
    
    print(total)
    return total

all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])