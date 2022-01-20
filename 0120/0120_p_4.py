def snail(height, daytime, night):
    distance_left = height
    day_cnt = 0
    while 1:
        day_cnt += 1
        distance_left -= daytime
        if distance_left <= 0:   
            return day_cnt
        distance_left += night
    
print(snail(100, 5, 2))