def get_middle_name(strs): # *args 로 받으면 함수 input이 콤마 단위로 투플 요소에 들어가게돼서
    alps = [alp for alp in strs] # ['apple', ] 이런식으로 저장됨
    cnt = 0

    for idx in alps:
        cnt += 1

    if cnt % 2: #홀수
        print(alps[cnt//2])    
    else: #홀수
        print(alps[cnt//2 - 1], alps[cnt//2])

get_middle_name('HELLo CPT')