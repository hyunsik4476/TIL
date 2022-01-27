def dict_invert(my_dict):
    new_dict = {}

    for key, value in my_dict.items():
        if value in new_dict:
            new_dict[value].append(key)
        else:
            new_dict[value] = [key]
            
    return new_dict

print(dict_invert({1: 10, 2: 20, 3: 30}))
print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))
print(dict_invert({1: True, 2: True, 3: True}))