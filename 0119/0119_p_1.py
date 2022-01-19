def function_name(**kwargs): # 권장되는 기입 형태
    # code block
    
    # return print(**kwargs) # 헷갈리지말기
    return print(kwargs)

# function_name('name': '홍길동', 'age': 999) # 잘못된 용례

function_name(name = '홍길동', age = 999) # 바른 용례 (이 때 name 과 age는 식별자)

# function_name() # 도 가능 (빈 딕셔너리 {} 리턴)

# kwargs 는 딕셔너리