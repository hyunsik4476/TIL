# 분할정복

## 퀵 소트

```python
def qsort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        qsort(A, l, s - 1)
        qsort(A, s + 1, r)


def partition(A, l, r):
    pivot = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j
```

* l : 피봇값보다 큰 값이 나올때까지 이동
* r: 피봇값보다 작은 값, 혹은 l 과 교차할때 까지 이동
  * 왜? l 과 r 이 교차하면 r은 피봇을 기준으로 큰 값과 작은 값의 사이에 위치함
* l 과 r 이 교차하면 lst[r] 과 피봇의 위치를 바꿈
  * 해당 피봇에 대해 정렬이 끝



## 머지소트 1

```python
def merge_sort(A):
    if len(A) <= 1:
        return A
    left_lst = []
    right_lst = []
    mid = len(A)//2
    for i in range(mid):
        left_lst.append(A[i])
    for j in range(mid, len(A)):
        right_lst.append(A[j])
    print(left_lst, right_lst)
    left_lst = merge_sort(left_lst)
    right_lst = merge_sort(right_lst)

    return merge(left_lst, right_lst)


def merge(left_lst, right_lst):
    result = []
    while len(left_lst) > 0 or len(right_lst) > 0:
        if len(left_lst) > 0 and len(right_lst) > 0:
            if left_lst[0] <= right_lst[0]:
                result.append(left_lst.pop(0))
            else:
                result.append(right_lst.pop(0))
        elif len(left_lst) > 0:
            result.append(left_lst.pop(0))
        elif len(right_lst) > 0:
            result.append(right_lst.pop(0))

    return result
```

## 머지소트 2

```python
def merge_sort(A):
    if len(A) <= 1:
        return A

    mid = len(A)//2
    left_lst = [0]* mid
    right_lst = [0] * (len(A) - mid)

    for i in range(mid):
        left_lst[i] = A[i]
    for j in range(mid, len(A)):
        right_lst[j - mid] = A[j]
    left_lst = merge_sort(left_lst)
    right_lst = merge_sort(right_lst)

    return merge(left_lst, right_lst)


def merge(left_lst, right_lst):
    global cnt
    result = [0] * (len(left_lst) + len(right_lst))
    if left_lst[-1] > right_lst[-1]:
        cnt += 1

    i, j, k = 0, 0, 0
    while i < len(left_lst) or j < len(right_lst):

        if i < len(left_lst) and j < len(right_lst):
            if left_lst[i] <= right_lst[j]:
                result[k] = left_lst[i]
                i += 1
                k += 1
            else:
                result[k] = right_lst[j]
                j += 1
                k += 1
        elif len(left_lst) > i:
            result[k] = left_lst[i]
            i += 1
            k += 1
        elif len(right_lst) > j:
            result[k] = right_lst[j]
            j += 1
            k += 1

    return result
```

* 실행시간 문제로 인덱스 접근으로 변경
* 기본적으로 반 반 나눠서 양쪽 리스트의 첫 요소들끼리 비교함