def collatz(num):
    cnt = 0
    while (num - 1):
        if num % 2: # 홀수
            num = num * 3 + 1
        else:
            num = num / 2

        cnt += 1

        if cnt > 500:
            return -1
    
    return cnt

print(collatz(6))
print(collatz(16))
print(collatz(27))
print(collatz(626331))