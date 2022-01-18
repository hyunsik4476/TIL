number = int(input())
if 1000 >= number >= 1:
    aliq_lists = [num for num in range(1, number + 1) if number % num == 0]
    print(aliq_lists)
else:
    print('N은 1 이상 1000 이하의 정수입니다.')