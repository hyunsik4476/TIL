def count_vowels(str_input):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for vowel in vowels_list:
        cnt += str_input.count(vowel)
    print(cnt)

count_vowels('banana')