import datetime

YMD = '2022/01/21' # 이걸 편하게 쓸 방법 없을까?
YMD_list = list(map(int, YMD.split('/')))
print(YMD_list)
# d = datetime.datetime(YMD_list) # 안 됨, 투플도
d = datetime.date(YMD_list[0], YMD_list[1], YMD_list[2]) # 다른 방법 없나?
print(d.month)