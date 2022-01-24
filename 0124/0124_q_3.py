def only_square_area(list_1, list_2):
    return_list = []
    for num in list_1:
        if num in list_2:
            return_list.append(num ** 2)
    return return_list
