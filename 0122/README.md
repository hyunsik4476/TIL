# 복습

> 20220122

## range

``` python
num = int(input())

for i in range(num , -1, -1):
    print(i)
# num 에서 0 까지 출력 가능
```

## 언팩연산자

```python
num = 50

lst = [i for i in range(1, num + 1) if not num % i]

print(*lst, sep = ', ')
```

* 리스트에 언팩 연산자 * 붙여서 요소만 출력 가능

```python
for alp in lst_2:
    print(alp, end = ' ')
# for alp in *lst_2:
#     print(alp, end = ' ') # 안됨
```

```python
inum = 5
lst = []
strs = ''

for num in range(1, inum + 1):
    lst.append(num)
    strs = strs + str(num) + ' '
    print(*lst) # 정수 5개
    print(strs) # 문자열 
    
for alp in strs:
    print(alp) # 공백문자도 alp 하나로 취급돼서 10 줄 나옴
```

