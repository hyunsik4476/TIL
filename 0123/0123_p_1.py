def my_avg(*args):
    cnt = 0
    tot = 0
    
    for num in args:
        cnt += 1
        tot += num
    print(tot / cnt)
    print(sum(args)/ len(args))

# my_avg(map(int, input().split())) # 안 됨. map 과 int의 연산 불가능
my_avg(*list(map(int, input().split()))) # 되긴 함, 근데 굳이?