def quickSort(a, begin, end):
    if begin < end: # 정렬할 대상이 남아있으면
        p = partition(a, begin, end)    # 피봇의 위치를 정하는 파티셔닝
        quickSort(a, begin, p-1)        # 피봇 기준 좌, 우에 반복
        quickSort(a, p+1, end)


def partition(a, begin, end):   # (피봇 : 정렬 전 후 움직이지 않는 값) 찾기
    pivot = (begin + end) // 2  # 일단 하나 찍어서 피봇으로 정함
    L = begin       # 오른쪽으로 이동하면서 피봇 이상의 원소 찾기
    R = end         # 왼쪽으로 이동하면서 피봇 미만의 원소 찾기
    while L < R:    # L 과 R이 만날 때까지
        while L < R and a[L] < a[pivot]:
            L += 1
        while L < R and a[R] >= a[pivot]:
            R -= 1
        if L < R:   # 만나지 못하고 포인터가 멈추면 a[L]과 a[R]이 교환됨
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]
    # L과 R이 만나면, while이 종료
    a[pivot], a[R] = a[R], a[pivot] # L 과 R이 만난 지점이 피봇 위치
    return R        # 피봇의 위치 리턴
