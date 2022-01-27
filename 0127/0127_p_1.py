def tax(money):
    if 8800 >= money > 4600:
        return 582 + (money - 4600)*0.15
    elif 4600 >= money > 1200:
        return 72 + (money - 1200)*0.15
    else:
        return money*0.06
print(tax(1200))
print(tax(4600))
print(tax(5000))