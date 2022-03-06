# 평가 대비

## math 함수

[참고](https://docs.python.org/ko/3/library/math.html)

### math.isclose(a, b)

* True 혹은 False 반환



### 삼각함수

* math.sin(x)
  * x 라디안의 사인값을 반환
* math.asin(x)
  * x 아크사인으로 라디안을 반환(-pi/2 ~ pi/2)

* math.dist(a, b)
  * a, b 는 좌표 시퀀스(또는 이터러블) 두 점 a, b 사이의 유클리드 거리를 반환

!!!

* math.degrees(x)

* math.radians(x)

* ```python
  import math
  a = [0,0]
  b = [2,2]
  print(math.dist(a, b))
  print(math.hypot(*[3,4]))
  print(math.degrees(math.pi))
  # 2.8284271247461903
  # 5.0
  # 180.0
  ```

* atan 사용시 범위 조심(90도, 270도 기준으로 +- 잡는게 안전해보임)