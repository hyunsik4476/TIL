def duplicated_letters(input_str):
    lst = [alp for alp in input_str]
    alp_set = set()

    for alp in lst:
        if lst.count(alp) >= 2:
            alp_set.add(alp)

    return list(alp_set)

print(duplicated_letters('apppppppple'))
