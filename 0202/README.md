# 대비

## 2진수

* 0b1010110101
* bin(31)
* format(15, 'b')

## continue

* 컨티뉴 이후 문장 실행 안하고 다음 루프로

## for - else

* 반복문이 break 로 종료되면 else는 실행 안됨

## list 형변환

* list를 str로 형변환했을 때, []도 포함됨

## 재귀

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
```

## 딕셔너리 정렬

```python
a = {'a': 5, 'b': 2, 'c': 3}
b = sorted(a, key = a.get)
print(b)
>>> ['b', 'c', 'a']
```

```python
a = {'a': 5, 'b': 2, 'c': 3}
b = sorted(a.items(), key = lambda x: x[1])
print(b)
>>>[('b', 2), ('c', 3), ('a', 5)]
```

