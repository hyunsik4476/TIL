# 1. 최댓값과 그 등장 횟수 출력
# numbers = [7, 10, 22, 7, 22, 22]

# numbers_max = max(numbers)
# i = 0

# for i in numbers:
#     if i == numbers_max:
#         i += 1
        
# print(f'{numbers_max} {i}') #numbers_max + 1 이 출력됨 (초기화한 변수를 for 문에 사용)


# # 2. 주어진 단어에서 특정 알파벳 제거하기
# word = input()

# word_remove_a = (alp for alp in word if alp != 'a')
# strs = "".join(word_remove_a) #반복 가능한 객체를 문자열에 더함
# print(type(word_remove_a))
# print(strs)


# # 3. 최댓값 찾기
# numbers = [7, 10, 22, 4, 3, 17]

# max_num = numbers[0]

# # for i in range(len(numbers)-1):
# #     if max_num < numbers[i+1]:
# #         max_num = numbers[i+1]
# #     else:
# #         pass #지워도 됨
        
# # print(max_num)


# for i in numbers:
#     if max_num < i:
#         max_num = i
# print(max_num)

# # 4. 단어 뒤집기
# word = 'hello'
# word_reversed = ''

# for i in word:
#     word_reversed = i + word_reversed

# print(word_reversed)