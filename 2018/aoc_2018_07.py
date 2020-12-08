

f = open("./2018_07.txt")
lines = f.read().splitlines()

dep = [[0 for x in range(26)] for y in range(26)]
dep_count = [0 for x in range(26)]
time_avail = [0 for x in range(26)]
time_complete = [-1 for x in range(26)]
time_start = [-1 for x in range(26)]

for a in lines:
    x = ord(a[5])-65
    y = ord(a[36])-65
    dep[y][x] = 1
    dep_count[y] += 1

nq = 0

output = ""
final_t = 0
for t in range(3000):
    for i in range(26):
        if time_complete[i] == t:
            output += chr(i+65)
            final_t = t
            for j in range(26):
                if dep[j][i] == 1:
                    dep[j][i] = 0
                    dep_count[j] -= 1
                    time_avail[j] = t
            nq -= 1
    for i in range(26):
        if nq < 5 and time_avail[i] <= t and dep_count[i] == 0 and time_start[i] == -1:
            nq += 1
            time_start[i] = t
            time_complete[i] = t + 60 + 1 + i
    
print(output, final_t)

