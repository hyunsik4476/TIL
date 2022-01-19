def dict_list_sum(input_dict_list): # 딕셔너리라고 **kwargs 쓰지 말것
    total = 0

    for dict in input_dict_list:
        total += dict['age']

    print(total)
    return total

dict_list_sum([{'name': 'kim', 'age': 12}, 
                {'name': 'lee', 'age': 4}])