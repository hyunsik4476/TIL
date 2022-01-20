def my_any(elements):
    
    for element in elements:
        if element:
            return True
    
    return False

print(my_any([1, 2, 5, '6']))
print(my_any([[], 2, 5, '6']))
print(my_any([0]))
print(my_any([]))
print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any([0]), any([]))