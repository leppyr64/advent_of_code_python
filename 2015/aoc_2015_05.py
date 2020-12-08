from collections import defaultdict

f = open("./2015/2015_05.txt")
inp = f.read().splitlines()
f.close()



def has_three_vowels(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    if d['a'] + d['e'] + d['i'] + d['o'] + d['u'] >= 3:
        return True
    return False

def has_double_letter(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return True
    return False

def has_naughty_string(s):
    naughty = ['ab', 'cd', 'pq', 'xy']
    for i in range(1, len(s)):
        if s[i - 1: i + 1] in naughty:
            return True
    return False

def has_two_pairs(s):
    for i in range(1,len(s)):
        for j in range(i + 2, len(s)):
            if s[j - 1] == s[i - 1] and s[j] == s[i]:
                return True
    return False

def has_sep_letter(s):
    for i in range(2, len(s)):
        if s[i - 2] == s[i]:
            return True
    return False

part1 = 0
part2 = 0
for s in inp:
    if has_three_vowels(s) and has_double_letter(s) and has_naughty_string(s) == False:
        part1 += 1
    if has_two_pairs(s) and has_sep_letter(s):
        part2 += 1
print(part1, part2)