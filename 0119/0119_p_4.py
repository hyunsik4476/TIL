a = 'global a'
b = 'global b'
c = 'global c'

def en_fn():
    a = 'enclosed a'
    b = 'enclosed b'

    def lo_fn():
        a = 'local a'
        print(a, b, c)

    lo_fn()

    print(a, b, c)
    

en_fn()

print(a, b, c)