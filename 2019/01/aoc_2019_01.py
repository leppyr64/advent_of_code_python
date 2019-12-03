

def fuel_a(m):
    if m < 9:
        return(0)
    return(m // 3 - 2)

def fuel_b(m):
    if m < 9:
        return(0)
    return(m // 3 - 2 + fuel_b(m // 3 - 2))

f = open("./2019/01/2019_01.txt")
inp = f.read().splitlines()
f.close()
inp = [int(a) for a in inp]

sum_a = 0
sum_b = 0
for a in inp:
    sum_a += fuel_a(a)
    sum_b += fuel_b(a)
print (sum_a, sum_b)
