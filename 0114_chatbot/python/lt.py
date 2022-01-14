import random

def ltm(n):
    for i in range(n):
        print(random.sample(range(1, 46), 6))

ltm(int(input()))