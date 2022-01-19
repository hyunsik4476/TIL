def function_name(parameter_1, parameter_2, *args):
    # code block
    return print(parameter_1, parameter_2, args)

function_name('B', 'A') # 위치
function_name(parameter_2 = 'A', parameter_1 = 'B') # 키워드

# 위치 -> 키워드 가능 ex) 필수 arg.를 넣고 선택 arg.를 키워드로 지정
# 키워드 -> 위치 불가능 why?) 키워드로 지정한 순간 위치가 의미 없어짐

# 이 에러는 정의(필수/ 선택) 호출(위치/ 키워드) 모두 해당

# ============================================================== #

def function_name_2(parameter_1, *args, parameter_2):
    # code block
    return print(parameter_1, parameter_2, args)

# function_name_2('B', 'A') # 작동 안함
# function_name_2('B', 'C', 'D' ,'A') # 작동 안함
function_name_2('B', 'C', 'D' , parameter_2 = 'A') # 작동 함 >>> B A ('C, 'D')
function_name_2(parameter_2 = 'A', parameter_1 = 'B') # 작동 함 (왜???) >>> B A ()

# ============================================================== #

def function_name_3(parameter_1, parameter_3 = 'C', parameter_2): #SyntaxError: non-default argument follows default argument
    # code block
    return print(parameter_1, parameter_2, parameter_3)

function_name_3('B', 'A') # 작동 안함
function_name_3(parameter_2 = 'A', parameter_1 = 'B') # 작동 안함