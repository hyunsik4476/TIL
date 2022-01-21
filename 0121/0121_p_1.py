a = [1,2,3,4,5]
b = ['1','2','3','4','5']
d = {'1': 'a', '2': 'b', '3': 'c', '4': 'd'}
e = dict()
for key, value in d.items(): #키 밸류 뒤집기
    e[value] = key

print(sum(a), sum(map(int, b))) # map 객체도 sum 사용 가능
print(list(map(int, d))) # map 을 딕셔너리에 적용하면 key만 순회함
print(e.values()) #dict_values(['1', '2', '3', '4']) 출력
print(list(e.values())) # 리스트로 변환 가능
print(max(map(int, e.values()))) # map도 적용 가능