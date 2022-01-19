def my_avg(*args):
    # nums = [num for num in args]
    cnt = 0
    tot = 0

    for num in args: # 생각해보니 in nums일 필요가 있나?
        cnt += 1
        tot += num
    
    print(tot / cnt)

my_avg(77, 83, 95, 80, 70)