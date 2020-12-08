import queue

f = open("./2018/06/06input.txt")
inp = f.readlines()
f.close()


g = [[-1 for x in range(502)] for y in range(502)]
d = [[10000 for x in range(502)] for y in range(502)]
is_infinite = [0 for x in range(100)]
count = [0 for x in range(100)]

q = queue.Queue(maxsize=25000)

for i in range(len(inp)):
    r = int(inp[i].split(",")[0])
    c = int(inp[i].split(",")[1])
    g[r][c] = i
    d[r][c] = 0
    q.put(r*1000+c)

while not q.empty():
    a = q.get()
    c = a % 1000
    r = (a - c) // 1000
    if(g[r][c] != -1):
        if r == 0 or r == 501 or c == 0 or c == 501:
            is_infinite[g[r][c]] = 1
        else:
            count[g[r][c]] += 1
            if(d[r+1][c] == 10000):
                g[r+1][c] = g[r][c]
                d[r+1][c] = d[r][c] + 1
                q.put((r+1) * 1000 + (c))
            if(d[r-1][c] == 10000):
                g[r-1][c] = g[r][c]
                d[r-1][c] = d[r][c] + 1
                q.put((r-1) * 1000 + (c))
            if(d[r][c+1] == 10000):
                g[r][c+1] = g[r][c]
                d[r][c+1] = d[r][c] + 1
                q.put((r) * 1000 + (c+1))
            if(d[r][c-1] == 10000):
                g[r][c-1] = g[r][c]
                d[r][c-1] = d[r][c] + 1
                q.put((r) * 1000 + (c-1))

            if(d[r+1][c] == d[r][c] + 1 and g[r+1][c] != g[r][c]):
                g[r+1][c] = -1
            if(d[r-1][c] == d[r][c] + 1 and g[r-1][c] != g[r][c]):
                g[r-1][c] = -1
            if(d[r][c+1] == d[r][c] + 1 and g[r][c+1] != g[r][c]):
                g[r][c+1] = -1
            if(d[r][c-1] == d[r][c] + 1 and g[r][c-1] != g[r][c]):
                g[r][c-1] = -1
            
for i in range(100):
    print(i, is_infinite[i], count[i])


