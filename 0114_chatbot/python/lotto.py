# sample 함수를 쓰기 위한 모듈 불러오기
import random
# print(random.sample(range(1, 46), 6)) 형태로 한 줄로도 해결 가능

# 리스트 만들기

# ball_box = list(range(1, 46)) 가 훨씬 편함
ball_box = []
for i in range(1, 46):
    ball_box.append(i)

result = random.sample(ball_box, 6)

print(result)