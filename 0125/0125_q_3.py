def lonely(input_list):
    lst = [input_list[0]]    

    for i in range(len(input_list) - 1):
        if input_list[i] != input_list[i + 1]:
            lst.append(input_list[i + 1])
    return lst

print(lonely([1,3,1,1,0,1,1,2]))