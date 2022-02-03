a = {'a': 5, 'b': 2, 'c': 3}
b = sorted(a.items(), key = lambda x: x[1])
print(b)