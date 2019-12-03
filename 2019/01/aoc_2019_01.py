# Advent of Code 2019 - Day 1
# https://adventofcode.com/2019/day/1
# --- Day 1: The Tyranny of the Rocket Equation ---

# O(digits in input base 3)
# Maximum digits for 6 digit number in ternary is 13 so recursion is ok
# Dynamic programming is an ok option too

# Function for part A
def fuel_a(m):
    if m < 9:
        return(0)
    return(m // 3 - 2)

# Recursive solution for part B
def fuel_b(m):
    if m < 9:
        return(0)
    return(m // 3 - 2 + fuel_b(m // 3 - 2))

# Read Input
f = open("./2019/01/2019_01.txt")
inp = f.read().splitlines()
f.close()
inp = [int(a) for a in inp]

# Calculate solution - Lambdas are a topic to learn here
sum_a = 0
sum_b = 0
for a in inp:
    sum_a += fuel_a(a)
    sum_b += fuel_b(a)
print (sum_a, sum_b)

