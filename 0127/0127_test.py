def p_print(lsts):
    return_strs = ''
    if len(lsts):
        cnt = 1
        for lst in lsts:
            return_strs += f'{cnt} 조 : {lst}\n'
            cnt += 1
        return return_strs
    else:
        return '빈 리스트'

print(p_print(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']))