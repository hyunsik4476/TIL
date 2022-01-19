a = 'richam'

def ham():
    global a 
    a = 'spam'
        
print(a) # 'richam'
ham()
print(a) # 'spam'