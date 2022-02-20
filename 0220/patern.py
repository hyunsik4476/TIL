from platform import java_ver


text = input()
pattern = input()
N = len(text)
M = len(pattern)
i = 0
j = 0

while i < N and j < M:
    if text[i] != pattern[j]:
        i = i-j
        j = -1
    i += 1
    j += 1

if j == M:
    print(i-M)