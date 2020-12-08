from string import ascii_lowercase


def remaining_len(txt):
    changed = 1
    while changed == 1:
        changed = 0
        for i in range(len(txt)-1):
            if txt[i] != txt[i+1] and txt[i].lower() == txt[i+1].lower(): 
                #print(i, txt[i], txt[i+1])
                changed = 1
                txt = txt[0:i] + txt[i+2:]
                break;
    return len(txt)

def remove_polymer(txt, x):
    txt = txt.replace(x, "")
    txt = txt.replace(x.upper(), "")
    return txt;

f = open("2018_05.txt")
txt = f.readline()

for c in ascii_lowercase:
    print(c, remaining_len(remove_polymer(txt, c)))
