def count_blood(input_list):
    blood_list = ['A', 'B', 'AB', 'O']
    blood_dict = {}
    
    for blood in blood_list:
        blood_dict[blood] = input_list.count(blood)

    return blood_dict

    # A_cnt = input_list.count('A')
    # B_cnt = input_list.count('B')
    # AB_cnt = input_list.count('AB')
    # O_cnt = input_list.count('O')

    # blood_dict = {'A': A_cnt, 'B': B_cnt, 'AB': AB_cnt, 'O': O_cnt}
    # return blood_dict

    

print(count_blood(['A','B','AB','O','A','B','AB','O','A']))