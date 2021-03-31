# Advent of Code 2020 - Day 13
# https://adventofcode.com/2020/day/13


# A Python 3program to demonstrate 
# working of Chinise remainder 
# Theorem 
  
# Returns modulo inverse of a with 
# respect to m using extended 
# Euclid Algorithm. Refer below  
# post for details: 
# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/ 
def inv(a, m) : 
      
    m0 = m 
    x0 = 0
    x1 = 1
  
    if (m == 1) : 
        return 0
  
    # Apply extended Euclid Algorithm 
    while (a > 1) : 
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process  
        # same as euclid's algo 
        m = a % m 
        a = t 
  
        t = x0 
  
        x0 = x1 - q * x0 
  
        x1 = t 
      
    # Make x1 positive 
    if (x1 < 0) : 
        x1 = x1 + m0 
  
    return x1 
  
# k is size of num[] and rem[].  
# Returns the smallest 
# number x such that: 
# x % num[0] = rem[0], 
# x % num[1] = rem[1], 
# .................. 
# x % num[k-2] = rem[k-1] 
# Assumption: Numbers in num[]  
# are pairwise coprime 
# (gcd for every pair is 1) 
def findMinX(num, rem, k) : 
      
    # Compute product of all numbers 
    prod = 1
    for i in range(0, k) : 
        prod = prod * num[i] 
  
    # Initialize result 
    result = 0
  
    # Apply above formula 
    for i in range(0,k): 
        pp = prod // num[i] 
        result = result + rem[i] * inv(pp, num[i]) * pp 
      
      
    return result % prod 
  
# Driver method 
num = [3, 4, 5] 
rem = [2, 3, 1] 
k = len(num) 
print( "x is " , findMinX(num, rem, k)) 
  
# This code is contributed by Nikita Tiwari. 

def part1(inp):
    t0 = int(inp[0])
    inp = inp[1].split(',')

    n = -1
    tn = 1000000000000
    for x in inp:
        if  x != 'x':
            x = int(x)
            t1 = ((t0 // x) + 1) * x
            if t1 - t0 < tn - t0:
                tn = t1
                n = x
    return n, tn, (tn - t0) * n

def part2(inp):
    t0 = int(inp[0])
    inp = inp[1].split(',')
    num = []
    rem = []
    n = 0
    for i in range(len(inp)):
        if inp[i] != 'x':
            n += 1
            num.append(int(inp[i]))
            rem.append((int(inp[i])*10 - i) % int(inp[i]))
    print(num)
    print(rem)
    return findMinX(num, rem, n)


f = open('./2020/input/2020_13_small.txt')
lines = f.read().splitlines()
f.close()
print(part1(lines))
print(part2(lines))



f = open('./2020/input/2020_13.txt')
lines = f.read().splitlines()
f.close()
print(part1(lines))
print(part2(lines))


#print(part2(['0','17,x,13,19']))
#print(part2(['0','67,7,59,61']))
#print(part2(['0','67,x,7,59,61']))
#print(part2(['0','67,7,x,59,61']))
#print(part2(['0','1789,37,47,1889']))