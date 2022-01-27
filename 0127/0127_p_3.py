def start_end(words):
    cnt = 0

    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            cnt += 1
            
    return cnt

print(start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']))