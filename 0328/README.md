# 조합 알고리즘

## 1

```python
def nCr1(idx, r, tmp = []):
    global cnt1
    cnt1 += 1
    if len(tmp) == r:
        print(tmp)
        return
    else:
        for i in range(idx, len(lst)):
            nCr1(i+1, r, tmp + [lst[i]])
```



## 2

```python
def nCr2(n, r, idx):
    global cnt2
    cnt2 += 1
    if r == 0:
        # print(result)
        return
    else:
        for i in range(idx, n-r+1):
            result[r-1] = lst[i]
            nCr(n, r-1, i+1)
```

* 1, 2 : 하나를 뽑고 그 다음 부분에 대해 뽑기 진행



## 3

```python
def nCr3(n, r):
    global cnt3
    cnt3 += 1
    if r == 0:
        # print(result2)
        return
    elif r > n:
        return
    else:
        result2[r-1] = lst[n-1]
        nCr2(n-1, r-1)
        nCr2(n-1, r)
```

* 콤비네이션 연산의 경우, 한 원소에 대해 해당 원소를 포함한 나머지의 조합 + 해당 원소를 포함하지 않는 나머지 원소의 조합으로 표현 가능
* nC0 = 1 이므로 재귀표현이 가능

