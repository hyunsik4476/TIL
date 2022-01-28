a = [{'a': 1, 'b': 2, 'c': 4, 'd': 3}, {'a': 1, 'b': 2, 'c': 4, 'd': 1}]

b = sorted(a, key = lambda x: x['d'], reverse= True)
a[0]['e'] = a[0].get('e', 0) + 1
print(a)