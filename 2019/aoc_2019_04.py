import re
from datetime import datetime
start=datetime.now()






def increasing(s):
    for i in range(1, len(s)):
        if s[i] < s[i-1]:
            return False
    return True

def has_pair_regex(s, part):
    x = re.findall(r'((\d)\2+)', s)
    if x == []:
        return False
    x = min([len(a[0]) for a in x])
    if part == 1 and x >= 2:
        return True
    elif part == 2 and x == 2:
        return True
    else:
        return False

def has_pair(s, part):
    s = 'x' + s + 'x'
    for i in range(1, len(s)-2):
        if part == 1 and s[i] == s[i+1]:
            return True
        elif part == 2 and s[i] != s[i-1] and s[i] == s[i+1] and s[i] != s[i+2]:
            return True
    return False

def is_valid(s, part):
    return increasing(s) and has_pair_regex(s, part)

def is_valid_new(s, part):
    return has_pair_regex(s,part)

count = [0,0,0]
#for z in range(246540,787420):
#    for p in range(1,3):
#        if is_valid(str(z), p):
#            count[p] += 1

for a in range(1,10):
    for b in range(a,10):
        for c in range(b,10):
            for d in range(c,10):
                for e in range(d,10):
                    for f in range(e,10):
                        x = a * 100000 + b * 10000 + c * 1000 + d * 100 + e * 10 + f
                        for p in range(1,3):
                            if is_valid_new(str(x), p):
                                count[p] += 1

print(count[1], count[2])

print (datetime.now()-start)