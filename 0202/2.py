a = [1,2,3]
b = [4,5,6]
c = list(zip(a, b))
print(sum([sum(tup) for tup in c]))