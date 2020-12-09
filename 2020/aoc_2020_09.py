
def find_first_invalid(nums, preamble):
    for i in range(preamble, len(nums)):
        found = False
        for j in range(i - preamble, i):
            for k in range(j + 1, i):
                if nums[j] + nums[k] == nums[i]:
                    found = True
        if found == False:
            return nums[i]
    return -1

def find_sum(nums, sumtofind):
    for i in range(len(nums)):
        for j in range(i):
            s = 0
            mx = -1
            mn = 1000000000000000
            for k in range(j, i + 1):
                mx = max(mx, nums[k])
                mn = min(mn, nums[k])
                s += nums[k]
            if s == sumtofind:
                return mn, mx
    return -1
            
f = open("./2020/input/2020_09.txt")
inp = f.read().splitlines()
f.close()
inp = [int(x) for x in inp]

z = find_first_invalid(inp, 25)
print('Part1', z)
y = find_sum(inp, z)
print('Part2', y[0] + y[1])

