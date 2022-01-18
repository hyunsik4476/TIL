number = int(input())

num_list = [(num + 1) for num in range(number)]
# rev_num_list = []

for idx in num_list: #인덱스 1부터 시작
    # rev_num_list.append(num_list[-idx])
    print(num_list[-idx])