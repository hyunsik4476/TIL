# 재귀함수
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) 
        
# 팩토리얼 함수 안에서 팩토리얼 함수 호출
# 함수는 return 값이 정해져야 종료될 수 있으므로
# n, n - 1, ... , 1 로 수렴해 base case에 도달 (factorial(1))