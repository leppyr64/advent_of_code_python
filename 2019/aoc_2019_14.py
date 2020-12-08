from collections import deque

f = open("./2019/2019_14.txt")
inp = f.read().splitlines()
f.close()

recipes = dict()
inventory = dict()
created = dict()


def dfs(e, n):
    if inventory[e] >= n:
        inventory[e] -= n
        n = 0
    elif inventory[e] > 0:
        n -= inventory[e]
        inventory[e] = 0

    if e == "ORE":
        created["ORE"] += n
        return

    nr = recipes[e]["n"]
    fullstacks = n // nr
    if n % nr != 0:
        fullstacks += 1
    
    for c in recipes[e]["children"]:
        nc = c[0]
        x = c[1]
        dfs(x, nc * fullstacks)
    
    created[e] += fullstacks * nr
    inventory[e] += fullstacks * nr - n

created["ORE"] = 0
inventory["ORE"] = 0

for a in inp:
    x, e = a.split("=")
    e = e[2:]
    ne, e = e.split(" ")
    x = x.strip()
    x = x.split(",")
    recipes[e] = {"n": int(ne), "children": []}
    created[e] = 0
    inventory[e] = 0
    for y in x:
        nc, c = y.strip().split(" ")
        recipes[e]["children"].append([int(nc), c])

dfs("FUEL", 1670300)


print("ORE", created["ORE"])
    
    # 1000000000000
    # 5986949044898 10000000
    # 2993474627157  5000000
    #  598695180524  1000000
    #  898042514063  1500000
    #  957911945216  1600000
    #  999820608393  1670000
    #  999999722750  1670299 
